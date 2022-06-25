const state = () => ({
  telegramUser: null
})


const getters = {
  isAuthenticated: (state) => {
    return state.telegramUser !== null
  }
}


const actions = {
  logoutUser({ state, commit }) {
    commit("setTelegramUser", null);
  },
  loginTelegramUser({ state, commit }, data) {
    commit("setTelegramUser", data);
  }
}


const mutations = {
  setTelegramUser(state, user) {
    state.telegramUser = user
  },
}


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}