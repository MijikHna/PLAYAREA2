<template>
  <v-container v-if="table" fluid class="excel-table">
    <div
      ref="table"
      id="table"
      :tabindex="'0'"
      @keydown.left="moveLeft"
      @keydown.right="moveRight"
      @keydown.up="moveUp"
      @keydown.down="moveDown"
      @keydown.enter="selectMode(mode.EDIT, selectedCell)"
      @keydown.esc="selectMode(mode.SELECT, selectedCell)"
      @keydown.tab="selectCell($event)"
    >
      <v-row class="d-table-row">
        <IndexCell
          :cellDesc="''"
          :initCellWidth="25"
          :initCellHeight="20"
          class="d-table-cell"
        ></IndexCell>

        <IndexCell
          v-for="(column, index) in table.columns"
          :key="index"
          :cellDesc="column.notation"
          :initCellWidth="100"
          :initCellHeight="20"
          :content="column.notation"
          class="d-table-cell"
        >
        </IndexCell>

        <AddColumnCell class="d-table-cell" />
      </v-row>

      <v-row
        v-for="(row, indexRow) in table.rows"
        :key="indexRow"
        class="d-table-row"
      >
        <IndexCell
          :initCellWidth="25"
          :initCellHeight="25"
          :content="row.number"
          class="d-table-cell"
        >
        </IndexCell>

        <Cell
          v-for="(column, indexCell) in table.columns"
          :key="indexCell"
          :cell="table.cells[indexRow * table.columns.length + indexCell]"
          class="d-table-cell"
          :ref="`${
            table.cells[indexRow * table.columns.length + indexCell].row
          }-${table.cells[indexRow * table.columns.length + indexCell].col}`"
          @modeSelected="selectMode"
          @tabPressed="selectCell"
          @cellContentUpdated="updateCellContent"
        ></Cell>
      </v-row>

      <v-row class="d-table-row">
        <AddRowCell class="d-table-cell" />
      </v-row>
    </div>
  </v-container>
</template>

<script>
import Cell from "./Cells/Cell.vue";
import IndexCell from "./Cells/IndexCell.vue";
import AddColumnCell from "./Cells/AddColumnCell.vue";
import AddRowCell from "./Cells/AddRowCell.vue";

import { mode } from "../js/constants.js";

export default {
  name: "Table",
  components: {
    Cell,
    IndexCell,
    AddColumnCell,
    AddRowCell,
  },
  data: () => {
    return {
      mode: { ...mode },
      selectedCell: null,
    };
  },
  computed: {
    table() {
      return this.$store.getters.table;
    },
  },
  methods: {
    selectMode(mode, cell) {
      if (this.selectedCell?.mode) {
        this.selectedCell.mode = mode.NONE;
      }

      this.selectedCell = this.$store.getters.getCellById(cell.id);

      this.selectedCell.mode = mode;

      if (mode === this.mode.SELECT) {
        setTimeout(() => {
          this.$refs.table.focus();
        }, 0);
        return;
      }

      const newActiveElem =
        this.$refs[`${this.selectedCell.row}-${this.selectedCell.col}`][0];
      setTimeout(() => {
        newActiveElem.$refs["the-cell"].focus();
      }, 0);
    },
    moveLeft() {
      if (!this.selectedCell || this.selectedCell.mode !== mode.SELECT) {
        return;
      }

      const currentCellRowId = this.selectedCell.row;
      const currentCellColumnId = this.selectedCell.col;

      if (currentCellColumnId === this.$store.getters.getTableFirstColId) {
        return;
      }

      this.selectedCell.mode = mode.NONE;

      const newSelectedCell = this.$store.getters.getCellByRowIdAndColumnId(
        currentCellColumnId - 1,
        currentCellRowId
      );

      this.selectMode(mode.SELECT, newSelectedCell);
    },
    moveRight() {
      if (!this.selectedCell || this.selectedCell.mode !== mode.SELECT) {
        return;
      }

      const currentCellRowId = this.selectedCell.row;
      const currentCellColumnId = this.selectedCell.col;

      if (currentCellColumnId === this.$store.getters.getTableLastColId) {
        return;
      }

      this.selectedCell.mode = mode.NONE;

      const newSelectedCell = this.$store.getters.getCellByRowIdAndColumnId(
        currentCellColumnId + 1,
        currentCellRowId
      );

      this.selectMode(mode.SELECT, newSelectedCell);
    },
    moveUp() {
      if (!this.selectedCell || this.selectedCell.mode !== mode.SELECT) {
        return;
      }

      const currentCellRowId = this.selectedCell.row;
      const currentCellColumnId = this.selectedCell.col;

      if (currentCellRowId === this.$store.getters.getTableFirstRowId) {
        return;
      }

      this.selectedCell.mode = mode.NONE;

      const newSelectedCell = this.$store.getters.getCellByRowIdAndColumnId(
        currentCellColumnId,
        currentCellRowId - 1
      );

      this.selectMode(mode.SELECT, newSelectedCell);
    },
    moveDown() {
      if (!this.selectedCell || this.selectedCell.mode !== mode.SELECT) {
        return;
      }

      const currentCellRowId = this.selectedCell.row;
      const currentCellColumnId = this.selectedCell.col;

      if (currentCellRowId === this.$store.getters.getTableLastRowId) {
        return;
      }

      this.selectedCell.mode = mode.NONE;

      const newSelectedCell = this.$store.getters.getCellByRowIdAndColumnId(
        currentCellColumnId,
        currentCellRowId + 1
      );

      this.selectMode(mode.SELECT, newSelectedCell);
    },
    selectCell(event) {
      event.preventDefault();
      event.stopPropagation();

      if (event.shiftKey) {
        this.moveLeft();
      } else {
        this.moveRight();
      }

      if (event.target !== this.$refs.table) {
        this.selectMode(mode.EDIT, this.selectedCell);
      }
    },
    updateCellContent(cell, newCellContent) {
      const theCell = this.$store.getters.getCellById(cell.id);

      theCell.content = newCellContent;
    },
  },
};
</script>

<style scoped>
.excel-table {
  overflow-x: auto;
}
#table {
  outline: none;
}
</style>