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
            <a-icon type="home"/>
            <span>主页</span>
          </a-menu-item>

          <a-menu-item key="send">
            <a-icon type="mail"/>
            <span>发送短信</span>
          </a-menu-item>

          <a-sub-menu>
            <span slot="title">
              <a-icon type="inbox"/>
              <span>发件箱</span>
            </span>
            <a-menu-item key="2">
              <a-icon type="file"/>
              <span>定时发件箱</span>
            </a-menu-item>
            <a-menu-item key="3">
              <a-icon type="file"/>
              <span>已发信箱</span>
            </a-menu-item>
          </a-sub-menu>

          <a-menu-item key="4">
            <a-icon type="inbox"/>
            <span>收件箱</span>
          </a-menu-item>

          <a-sub-menu>
            <span slot="title">
              <a-icon type="contacts"/>
              <span>通讯录</span>
            </span>
            <a-menu-item key="6">
              <a-icon type="user-add"/>
              <span>个人通讯录管理</span>
            </a-menu-item>
            <a-menu-item key="8">
              <a-icon type="usergroup-add"/>
              <span>公共通讯录管理</span>
            </a-menu-item>
          </a-sub-menu>

          <a-menu-item key="9">
            <a-icon type="logout"/>
            <span>退出</span>
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
      :visible="LoginFormVisible"
      :closable="false"
      :maskClosable="false"
      :destroyOnClose="true"
      @ok="handleSubmit"
      :confirmLoading="LoginFormConfirmLoading"
    >
      <a-form id="components-form-demo-normal-login" :form="LoginForm" class="login-form">
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
              <img src="@/assets/captcha.jpg" alt>
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
          :loading="LoginFormConfirmLoading"
          @click="handleSubmit"
        >登录</a-button>
      </template>
    </a-modal>
  </main>
</template>

<script>
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

export default {
  data() {
    return {
      decorators,
      LoginFormVisible: true,
      LoginFormConfirmLoading: false
    };
  },
  methods: {
    handleCancel() {},
    handelMenuSelect({ key }) {
      console.log(`SELECT: push to ${key}`);
      this.$router.push({ name: key });
    },
    handleSubmit() {
      this.LoginFormConfirmLoading = true;
      this.LoginForm.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
          this.LoginFormVisible = false;
        }
        this.LoginFormConfirmLoading = false;
      });
    }
  },
  beforeCreate() {
    this.LoginForm = this.$form.createForm(this);
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

