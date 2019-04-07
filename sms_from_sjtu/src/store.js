import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    headers: [],
    data: [],
    pkey: '',
    useTemplate: false,
    template: ''
  },
  getters: {
    columns(state) {
      return state.headers.map(head => {
        return {
          title: head,
          dataIndex: head
        }
      })
    },
    renderTemplateSMS(state) {
      return function(row) {
        let s = state.template
        for (let [k, v] of Object.entries(row)) {
          s = s.replace(`{${k}}`, v)
        }
        return s
      }
    },
    getPhoneNumber(state) {
      return function(row) {
        return row[state.pkey]
      }
    }
  },
  mutations: {
    headers(state, headers) {
      state.headers = headers
    },
    data(state, data) {
      state.data = data
    },
    pkey(state, pkey) {
      state.pkey = pkey
    },
    useTemplate(state, useTemplate) {
      state.useTemplate = useTemplate
    },
    template(state, template) {
      state.template = template
    }
  }
})
