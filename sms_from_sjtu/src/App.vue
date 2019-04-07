<template>
  <main id="app">
    <a-layout id="components-layout-demo-side" style="min-height: 100vh">
      <a-layout-header>
        <a-menu
          theme="dark"
          mode="horizontal"
          :style="{ lineHeight: '64px', float: 'right' }"
          :defaultSelectedKeys="['1']"
          @select="handelMenuSelect"
        >
          <a-menu-item key="home">
            <a-icon type="mail"/>
            <span>发信</span>
          </a-menu-item>

          <a-menu-item key="send">
            <a-icon type="mail"/>
            <span>发送短信</span>
          </a-menu-item>

          <a-menu-item key="receive">
            <a-icon type="inbox"/>
            <span>收信</span>
          </a-menu-item>

          <a-menu-item key="9">
            <a-icon type="logout"/>
            <span>注销</span>
          </a-menu-item>
        </a-menu>
      </a-layout-header>

      <a-layout>
        <a-layout-content>
          <div class="container">
            <router-view/>
          </div>
        </a-layout-content>
      </a-layout>
    </a-layout>

    <a-modal
      title="登录"
      :visible="formVisible"
      :closable="false"
      :maskClosable="false"
      :destroyOnClose="true"
      @ok="handleSubmit"
      :confirmLoading="formConfirmLoading"
    >
      <a-form id="components-form-demo-normal-login" :form="form" class="login-form">
        <a-form-item>
          <a-input size="large" v-decorator="decorators.username" placeholder="jAccount用户名">
            <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)"/>
          </a-input>
        </a-form-item>

        <a-form-item>
          <a-input
            size="large"
            v-decorator="decorators.password"
            type="password"
            placeholder="jAccount密码"
          >
            <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)"/>
          </a-input>
        </a-form-item>

        <a-form-item>
          <a-row :gutter="8">
            <a-col :span="12">
              <a-input size="large" v-decorator="decorators.captcha" placeholder="验证码">
                <a-icon slot="prefix" type="safety-certificate" style="color: rgba(0,0,0,.25)"/>
              </a-input>
            </a-col>
            <a-col :span="12">
              <img :src="captchaUri" @click="refreshCaptcha" style="cursor: pointer">
            </a-col>
          </a-row>
        </a-form-item>

        <a-form-item>
          <a-checkbox v-decorator="decorators.remember">保存我的账户信息</a-checkbox>
        </a-form-item>
      </a-form>
      <template slot="footer">
        <a-button
          key="submit"
          type="primary"
          html-type="submit"
          :loading="formConfirmLoading"
          @click="handleSubmit"
        >登录</a-button>
      </template>
    </a-modal>
  </main>
</template>

<script>
import { getCaptcha, submitCredentials } from "@/rpc";

export default {
  name: "app",
  data() {
    const decorators = {
      username: [
        "username",
        { rules: [{ required: true, message: "请输入你的jAccount用户名" }] }
      ],
      password: [
        "password",
        { rules: [{ required: true, message: "请输入你的密码" }] }
      ],
      captcha: [
        "captcha",
        { rules: [{ required: true, message: "请输入验证码" }] }
      ],
      remember: [
        "remember",
        {
          valuePropName: "checked",
          initialValue: false
        }
      ]
    };
    return {
      decorators,
      form: this.$form.createForm(this),
      formVisible: false,
      formConfirmLoading: false,
      captchaUri: ""
    };
  },
  methods: {
    handleCancel() {},
    handelMenuSelect({ key }) {
      console.log(`SELECT: push to ${key}`);
      this.$router.push({ name: key });
    },
    handleSubmit() {
      this.formConfirmLoading = true;
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
          submitCredentials(values)
            .then(rsp => {
              const { success, message } = rsp;
              if (success) {
                this.formVisible = false;
              } else {
                this.$message.error(message);
                this.refreshCaptcha();
              }
            })
            .catch(err => {
              this.$message.error(err);
              console.error(err);
              this.refreshCaptcha();
            })
            .finally(() => {
              this.formConfirmLoading = false;
            });
        }
      });
    },
    refreshCaptcha() {
      console.log("refreshCaptcha");
      getCaptcha()
        .then(uri => {
          console.log("response", uri);
          this.captchaUri = uri;
        })
        .catch(err => {
          this.$message.error(err);
          console.error(err);
        });
    }
  },
  beforeMount() {
    this.refreshCaptcha();
  }
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>

