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
        rowKey="__rowNum__"
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
              <div v-if="received[row[pkey]]">
                <p
                  v-for="{message, phone, sendTime} in received[row[pkey]]"
                  :key="`received-from-${phone}-${sendTime}`"
                >{{ message }}</p>
              </div>
            </fieldset>
          </a-col>
        </a-row>
        <span slot="customFooter">
          <a-icon type="smile-o"/>Name
        </span>
      </a-table>
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
      received: {},
      targetKeys: [],
      paginationOptions: {
        simple: false,
        showSizeChanger: true,
        hideOnSinglePage: true,
        defaultPageSize: 20,
        pageSizeOptions: ["10", "20", "30", "50", "100", "200"]
      }
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
      template: "template"
    }),
    receiveid: {
      get() {
        return parseInt(this.$store.state.receiveid);
      },
      set(value) {
        this.$store.commit("receiveid", String(value));
      }
    },
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
      return this.data.map(row => {
        let obj = Object.assign({}, row);

        if (this.received[this.getPhoneNumber(row)]) {
          obj["reply"] = "是";
        } else {
          obj["reply"] = "否";
        }

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
    }
  },
  mounted() {
    let timer = setInterval(() => {
      if (this.receiveid) {
        recieveMessage(String(this.receiveid))
          .then(response => {
            const { phone } = response;
            if (phone !== "") {
              this.receiveid = this.receiveid + 1;
              if (this.received[phone]) {
                this.$set(this.received, phone, [
                  ...this.received[phone],
                  response
                ]);
              } else {
                this.$set(this.received, phone, [response]);
              }
              // this.received.__ob__.dep.notify();
              // console.log(this.ProccessedData);
            }
          })
          .catch(err => {
            console.error(err);
          });
      }
    }, 10000);
  }
};
</script>
