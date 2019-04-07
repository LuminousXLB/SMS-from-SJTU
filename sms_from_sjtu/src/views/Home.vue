<template>
  <div class="home">
    <h1 style="margin: 1em;">导入数据</h1>

    <h2 style="margin: 1em;">选择一个工作簿</h2>
    <div>
      <a-upload-dragger
        name="file"
        accept=".xls, .xlsx, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        :beforeUpload="beforeUpload"
      >
        <!-- @change="handleStateChange" -->
        <p class="ant-upload-drag-icon">
          <a-icon type="inbox"/>
        </p>
        <p class="ant-upload-text">点击此处选择文件或拖拽文件到此处</p>
        <p class="ant-upload-hint">
          可以选择一个Excel文件，该文件中
          <strong>不能存在合并的单元格</strong>
        </p>
      </a-upload-dragger>
    </div>

    <h2 style="margin: 1em;">选择一个工作表</h2>
    <div v-if="workbook">
      <a-radio-group v-model="sheetName" @change="handleSheetChange">
        <a-radio-button
          v-for="item in workbook.SheetNames"
          :value="item"
          :key="`${path}_${item}`"
        >{{ item }}</a-radio-button>
      </a-radio-group>
    </div>

    <h2 style="margin: 1em;">选择表头模式</h2>
    <div v-if="worksheet">
      <a-radio-group v-model="headerMode">
        <a-radio-button :value="1">第一行作为表头</a-radio-button>
        <a-radio-button :value="2">使用默认表头</a-radio-button>
        <a-radio-button :value="3">自定义表头</a-radio-button>
      </a-radio-group>
    </div>
    <div v-if="headerMode===3">
      <a-input
        v-for="(item, index) in firstRawColumn"
        :key="`header-${index}`"
        :placeholder="item"
        v-model="headerInput[index]"
      ></a-input>
    </div>

    <h2 style="margin: 1em;">数据预览</h2>
    <div v-if="worksheet">
      <a-table :columns="columns" :dataSource="data" size="small" rowKey="__rowNum__" bordered/>
    </div>

    <h2 style="margin: 1em;">选择手机号码所在列</h2>
    <div v-if="worksheet">
      <a-radio-group v-model="phoneColumn">
        <a-radio-button v-for="item in headers" :value="item" :key="`header-${item}`">{{ item }}</a-radio-button>
      </a-radio-group>
    </div>

    <h2 style="margin: 1em;">手机号校验记录</h2>
    <div v-if="phoneColumn">
      <a-table
        :columns="columns"
        :dataSource="validate.wrong"
        size="small"
        rowKey="__rowNum__"
        bordered
      >
        <template slot="title">
          <h3>
            校验失败
            <sub>以下记录不会被发送短信</sub>
          </h3>
        </template>
      </a-table>

      <a-table
        :columns="columns"
        :dataSource="validate.correct"
        size="small"
        rowKey="__rowNum__"
        bordered
      >
        <template slot="title">
          <h3>
            校验成功
            <sub>将要使用以下记录发送短信</sub>
          </h3>
        </template>
      </a-table>
    </div>

    <h2 style="margin: 1em;">短信内容</h2>
    <div>
      <a-textarea rows="5" v-model="smsContentInput"/>
      <div>
        <span style="margin: 1em">是否使用模板</span>
        <a-switch v-model="useTemplate"/>
        <span style="margin: 1em">
          如使用模板，请用大括号包裹字段名，如
          <pre style="display: inline">{Name}</pre>
        </span>
      </div>
      <a-textarea v-if="useTemplate" rows="5" v-model="smsContentSample" readonly/>
    </div>

    <hr>
    <div style="margin: 1em;">
      <center>
        <a-button type="primary" size="large" @click="submit">确定</a-button>
      </center>
    </div>
  </div>
</template>

<script>
import XLSX from "xlsx";

const phonereg = new RegExp("^1\\d{10}$");

export default {
  name: "home",
  data() {
    return {
      path: "",
      workbook: undefined,
      worksheet: undefined,
      sheetName: "",
      headerMode: 1,
      headerInput: []
    };
  },
  computed: {
    smsContentSample() {
      if (this.validate && this.validate.correct.length > 0) {
        return this.renderTemplateSMS(this.validate.correct[0]);
      } else {
        return "";
      }
    },
    validate() {
      let wrong = [];
      let correct = [];
      if (this.data && this.data.length > 0) {
        for (let item of this.data) {
          if (!phonereg.test(item[this.phoneColumn])) {
            wrong.push(item);
          } else {
            correct.push(item);
          }
        }
      }
      return { wrong, correct };
    },
    data() {
      if (this.worksheet) {
        const header_options = [undefined, undefined, "A", this.headerInput];
        return XLSX.utils.sheet_to_json(this.worksheet, {
          header: header_options[this.headerMode],
          defval: ""
        });
      } else {
        return undefined;
      }
    },
    firstRawColumn() {
      if (this.worksheet) {
        let table = XLSX.utils.sheet_to_json(this.worksheet, {
          header: 1,
          defval: ""
        });
        return table[0];
      } else {
        return [];
      }
    },
    columns() {
      // STORE
      return this.$store.getters.columns;
    },
    phoneColumn: {
      // STORE
      get() {
        return this.$store.state.pkey;
      },
      set(value) {
        this.$store.commit("pkey", value);
      }
    },
    headers: {
      // STORE
      get() {
        return this.$store.state.headers;
      },
      set(value) {
        this.$store.commit("headers", value);
      }
    },
    useTemplate: {
      // STORE
      get() {
        return this.$store.state.useTemplate;
      },
      set(value) {
        this.$store.commit("useTemplate", value);
      }
    },
    smsContentInput: {
      // STORE
      get() {
        return this.$store.state.template;
      },
      set(value) {
        this.$store.commit("template", value);
      }
    }
  },
  methods: {
    submit() {
      const data = this.validate.correct;
      this.$store.commit("data", data);

      if (this.useTemplate) {
        const form = data.map(row => {
          return {
            phone: this.getPhoneNumber(row),
            message: this.renderTemplateSMS(row)
          };
        });

        console.log("send message with template", form);
      } else {
        const form = {
          phone: data.map(this.getPhoneNumber),
          message: this.template
        };

        console.log("send message without template", form);
      }
    },
    beforeUpload(file) {
      this.path = file.path;
      this.workbook = XLSX.readFile(this.path);
      this.sheetName = "";
      return false;
    },
    handleSheetChange(e) {
      this.headerMode = 0;
      if (this.workbook) {
        this.worksheet = this.workbook.Sheets[this.sheetName];
      } else {
        this.worksheet = undefined;
      }
    },
    renderTemplateSMS(row) {
      return this.$store.getters.renderTemplateSMS(row);
    },
    getPhoneNumber(row) {
      return this.$store.getters.getPhoneNumber(row);
    }
  },
  watch: {
    data(val, oval) {
      this.phoneColumn = "";
      if (val && val.length > 0) {
        this.headers = Object.keys(val[0]);
      } else {
        this.headers = [];
      }
    }
  }
};
</script>
