import Vue from 'vue';
import App from './App.vue';
import router from './router';

import { Form } from 'ant-design-vue';
Vue.use(Form);

import { Layout } from 'ant-design-vue';
Vue.use(Layout);

import { Menu } from 'ant-design-vue';
Vue.use(Menu);

import { Button } from 'ant-design-vue';
Vue.component(Button.name, Button);

import { Checkbox } from 'ant-design-vue';
Vue.component(Checkbox.name, Checkbox);

import { Col } from 'ant-design-vue';
Vue.component(Col.name, Col);

import { Row } from 'ant-design-vue';
Vue.component(Row.name, Row);

import { Icon } from 'ant-design-vue';
Vue.component(Icon.name, Icon);

import { Input } from 'ant-design-vue';
Vue.component(Input.name, Input);

import { Modal } from 'ant-design-vue';
Vue.component(Modal.name, Modal);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
