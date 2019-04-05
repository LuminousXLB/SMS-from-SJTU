<template>
  <div class="send">
    <h1 style="margin: 1em;">发送短信</h1>
    <a-form :form="form" layout="vertical" @submit="handleSubmit">
      <a-form-item label="手机号" :extra="phoneLength">
        <a-row>
          <a-col :span="12">
            <a-textarea @change="updatePhoneNumbers" autosize/>
          </a-col>
          <a-col :span="12">
            <a-textarea v-decorator="decorators.phones" autosize disabled/>
          </a-col>
        </a-row>
      </a-form-item>

      <a-form-item label="短信内容" :extra="contentLength">
        <a-textarea
          v-decorator="decorators.content"
          @change="updateContentLength"
          :autosize="{ minRows: 4 }"
        />
      </a-form-item>

      <a-form-item label="定时发送">
        <a-row>
          <a-col :span="4">
            <a-switch v-decorator="decorators.istiming"/>
          </a-col>
          <a-col :span="20">
            <a-time-picker v-decorator="decorators.timing" :defaultOpenValue="moment()"/>
          </a-col>
        </a-row>
      </a-form-item>

      <a-form-item>
        <div style="margin:1em">
          <a-button type="primary" htmlType="submit">发送短信</a-button>
        </div>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import moment from "moment";

const decorators = {
  phones: [
    "phones",
    {
      rules: [{ required: true, message: "请输入一组手机号" }]
    }
  ],
  content: [
    "content",
    {
      rules: [{ required: true, message: "请输入短信内容" }]
    }
  ],
  istiming: ["istiming"],
  timing: ["timing"]
};

export default {
  name: "send",
  data() {
    return {
      decorators,
      form: this.$form.createForm(this),
      phones: [],
      contentLength: "",
      isTiming: false
    };
  },
  computed: {
    phoneLength() {
      return `您已输入${this.phones.length}个手机号码`;
    }
  },
  methods: {
    moment,
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
      });
    },
    updatePhoneNumbers(e) {
      this.phones = [...new Set(e.target.value.match(/1\d{10}/g) || [])];
      this.form.setFieldsValue({ phones: this.phones.join("\n") });
    },
    updateContentLength(e) {
      this.contentLength = `您已输入${e.target.value.length}字`;
    }
  }
};
</script>
