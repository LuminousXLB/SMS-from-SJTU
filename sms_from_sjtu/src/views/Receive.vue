<template>
  <div class="receive">
    <h1 style="margin: 1em;">收信</h1>

    <h2 style="margin: 1em;">数据展示选项</h2>
    <div>
      <a-transfer
        :dataSource="columns"
        :titles="['展示', '折叠']"
        :targetKeys="targetKeys"
        :render="item=>item.title"
        @change="handleChange"
      />
      <!-- :selectedKeys="selectedKeys"
        @selectChange="handleSelectChange"
      @scroll="handleScroll"-->
    </div>

    <h2 style="margin: 1em;">发信数据</h2>
    <div>
      <a-table
        :columns="SplitColumn"
        :dataSource="ProccessedData"
        size="small"
        bordered
        :pagination="paginationOptions"
      >
        <a-row slot="expandedRowRender" slot-scope="row">
          <a-col :span="8">
            <a-form layout="horizontal">
              <a-form-item
                v-for="item in targetKeys"
                :key="`${row[pkey]}-${item}`"
                :label="item"
                :label-col="{ span: 6 }"
                :wrapper-col="{ span: 18 }"
                style="margin-bottom: 0"
              >
                <span>{{ row[item] }}</span>
              </a-form-item>
            </a-form>
          </a-col>
          <a-col :span="8">
            <fieldset>
              <legend>发信内容</legend>
              <p>{{ renderTemplateSMS(row) }}</p>
            </fieldset>
          </a-col>
          <a-col :span="8">
            <fieldset>
              <legend>收信内容</legend>
              <div v-if="replies[row[pkey]]">
                <p
                  v-for="{message, phone, sendTime} in replies[row[pkey]]"
                  :key="`replies-from-${phone}-${sendTime}`"
                >{{ message }}</p>
              </div>
            </fieldset>
          </a-col>
        </a-row>
        <span slot="customFooter">
          <a-icon type="smile-o"/>Name
        </span>
      </a-table>
      <a-button @click="AbortReceivingMessage">终止收信</a-button>
      <a-button @click="DownloadReplies">下载回信</a-button>
    </div>
  </div>
</template>

<script>
import XLSX from "xlsx";
import { mapState } from "vuex";
import { recieveMessage } from "@/rpc";

export default {
  name: "receive",
  data() {
    return {
      targetKeys: [],
      paginationOptions: {
        simple: false,
        showSizeChanger: true,
        hideOnSinglePage: true,
        defaultPageSize: 20,
        pageSizeOptions: ["10", "20", "30", "50", "100", "200"]
      },
      busy: false,
      suspend: false
    };
  },
  computed: {
    columns() {
      return this.$store.getters.columns;
    },
    ...mapState({
      headers: "headers",
      data: "data",
      pkey: "pkey",
      useTemplate: "useTemplate",
      template: "template",
      receiveid: "receiveid",
      rawReplies: "replies"
    }),
    replies() {
      return this.$store.getters.getReplies;
    },
    // receiveid: {
    //   get() {
    //     return parseInt(this.$store.state.receiveid);
    //   },
    //   set(value) {
    //     console.log("Receive.vue", "set receiveid", value);
    //     if (value) {
    //       this.$store.commit("receiveid", String(value));
    //     } else {
    //       this.$store.commit("receiveid", undefined);
    //     }
    //   }
    // },
    SplitColumn() {
      let columns = this.headers
        .filter(x => {
          return !this.targetKeys.includes(x);
        })
        .map(x => {
          return {
            title: x,
            dataIndex: x,
            key: x
          };
        });

      columns.push({
        title: "已回复",
        dataIndex: "reply",
        key: "reply"
      });

      return columns;
    },
    ProccessedData() {
      return this.data.map((row, index) => {
        let obj = Object.assign({}, row);

        if (this.replies[this.getPhoneNumber(row)]) {
          obj["reply"] = "是";
        } else {
          obj["reply"] = "否";
        }

        obj["key"] = `display_data_${row[this.pkey]}`;

        return obj;
      });
    }
  },
  methods: {
    handleChange(targetKeys) {
      console.log(targetKeys);
      this.targetKeys = targetKeys;
    },
    getPhoneNumber(row) {
      return this.$store.getters.getPhoneNumber(row);
    },
    renderTemplateSMS(row) {
      if (this.useTemplate) {
        return this.$store.getters.renderTemplateSMS(row);
      } else {
        return this.template;
      }
    },
    AbortReceivingMessage() {
      this.busy = true;
    },
    receive() {
      if (this.receiveid) {
        this.busy = true;
        recieveMessage(String(this.receiveid))
          .then(() => {
            this.busy = false;
          })
          .catch(err => {
            console.error(err);
          });
      }
    },
    DownloadReplies() {
      const { dialog } = require("electron").remote;
      const fs = require("fs");
      let fn = dialog.showSaveDialog({
        filters: [{ name: "Comma Seperated Files", extensions: ["csv"] }]
      });
      if (!fn.endsWith(".csv")) {
        fn = fn + ".csv";
      }
      if (fn) {
        const ws = XLSX.utils.json_to_sheet(this.rawReplies);
        const stream = XLSX.stream.to_csv(ws);
        stream.pipe(fs.createWriteStream(fn));
      }
    }
  },
  watch: {
    busy(busy, oval) {
      console.log("busy", `from ${busy} to ${oval}`);
      if (!busy && !this.suspend) {
        window.setTimeout(this.receive, 5000);
      }
    }
  },
  mounted() {
    this.receive();
  }
};
</script>
