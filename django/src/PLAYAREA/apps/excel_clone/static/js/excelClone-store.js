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
    tableId: (state) => {
      return state.table?.id || null;
    },
    getTableFirstRowId: (state) => {
      return state.table?.rows[0].id;
    },
    getTableLastRowId: (state) => {
      return state.table?.rows[state.table.rows.length - 1].id;
    },
    getTableFirstColId: (state) => {
      return state.table?.columns[0].id;
    },
    getTableLastColId: (state) => {
      return state.table?.columns[state.table.rows.length - 1].id;
    },
    getCellById: (state) => (id) => {
      return state.table?.cells.find((cell) => cell.id == id);
    },
    getCellByRowIdAndColumnId: (state) => (colId, rowId) => {
      return state.table?.cells.find(
        (cell) => cell.row === rowId && cell.col === colId
      );
    },
  },
  mutations: {
    setTable(state, newTable) {
      newTable.cells.forEach((cell) => {
        cell.mode = null;
      });
      state.table = newTable;
    },
  },
});

export default excelCloneStore;
