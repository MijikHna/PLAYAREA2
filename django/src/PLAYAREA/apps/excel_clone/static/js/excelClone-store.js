import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const excelCloneStore = new Vuex.Store({
  state: {
    table: null,
  },
  getters: {
    table: (state) => {
      return state.table;
    },
    tableName: (state) => {
      return state.table?.name || null;
    },
  },
  mutations: {
    setTable(state, newTable) {
      state.table = newTable;
    },
  },
});

export default excelCloneStore;
