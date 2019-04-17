import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    headerMode: 1,
    headers: [],
    data: [],
    pkey: '',
    useTemplate: false,
    template: '',
    receiveid: '',
    replies: []
  },
  getters: {
    columns(state) {
      return state.headers.map(head => {
        return {
          title: head,
          dataIndex: head,
          key: head
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
        return String(row[state.pkey])
      }
    },
    getReplies(state) {
      let obj = {}
      for (let reply of state.replies) {
        const { phone } = reply
        if (obj[phone]) {
          obj[phone].push(reply)
        } else {
          obj[phone] = [reply]
        }
      }
      return obj
    }
  },
  mutations: {
    headerMode(state, headerMode) {
      state.headerMode = headerMode
    },
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
    },
    receiveid(state, receiveid) {
      state.receiveid = receiveid
    },
    reply(state, { id, time, phone, message }) {
      state.replies.push({ id, time, phone, message })
      if (phone && parseInt(id) >= parseInt(state.receiveid)) {
        state.receiveid = new String(parseInt(id) + 1)
      }
      console.log('commit', id, time, phone, message)
    }
  }
})
