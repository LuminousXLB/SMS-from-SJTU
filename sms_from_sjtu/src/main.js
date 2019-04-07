import { Form } from 'ant-design-vue'
import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'

Vue.use(Form)

import { Layout } from 'ant-design-vue'
Vue.use(Layout)

import { List } from 'ant-design-vue'
Vue.use(List)

import { Menu } from 'ant-design-vue'
Vue.use(Menu)

import { Input } from 'ant-design-vue'
Vue.use(Input)

import { Radio } from 'ant-design-vue'
Vue.use(Radio)

import { Table } from 'ant-design-vue'
Vue.use(Table)

import { Upload } from 'ant-design-vue'
Vue.use(Upload)

import { Button } from 'ant-design-vue'
Vue.component(Button.name, Button)

import { Checkbox } from 'ant-design-vue'
Vue.component(Checkbox.name, Checkbox)

import { Col } from 'ant-design-vue'
Vue.component(Col.name, Col)

import { Row } from 'ant-design-vue'
Vue.component(Row.name, Row)

import { Icon } from 'ant-design-vue'
Vue.component(Icon.name, Icon)

import { Modal } from 'ant-design-vue'
Vue.component(Modal.name, Modal)

import { Switch } from 'ant-design-vue'
Vue.component(Switch.name, Switch)

import { TimePicker } from 'ant-design-vue'
Vue.component(TimePicker.name, TimePicker)

import { message } from 'ant-design-vue'
Vue.prototype.$message = message

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
