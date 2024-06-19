import {createStore} from "vuex";
import axios from "axios";
export const store = createStore({
  state: {
    userToken: localStorage.getItem('token') ?? null,
    userInfo: {
      firstname: null,
      lastname: null,
      login: null,
      age: null,
      email: null,
      country: null,
      phone: null
    }
  },
  mutations: {
    UPDATE_USER_TOKEN (state, token) {
      if (token.length !== 0) {
        state.userToken = `Token ${token}`
        localStorage.setItem('token', state.userToken)
      } else {
        state.userToken = null
        localStorage.removeItem('token')
      }
      axios.defaults.headers.common['Authorization'] = state.userToken
    }
  },
  getters: {

  },
  actions: {

  },

})