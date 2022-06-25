const state = () => ({
  user: localStorage.getItem("tg-user") ? JSON.parse(localStorage.getItem("tg-user")) : null,
})


const getters = {
  loggedIn: (state) => {
    return state.user !== null
  }
}


const actions = {
  logout({ state, commit }) {
    commit("clearUser");
  },
  loginuser({ state, commit }, data) {
    commit("setUser", data);
  }
}


const mutations = {
  setUser(state, user) {
    state.user = user;

    localStorage.setItem("tg-user", JSON.stringify(user));
  },
  clearUser(state) {
    state.user = null;
    localStorage.removeItem("tg-user");
  }
}


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}