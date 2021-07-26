<template>
  <v-container v-if="table" fluid>
    <DescriptionRow :columns="table.columns"></DescriptionRow>

    <v-row
      v-for="(row, indexRow) in table.rows"
      :key="indexRow"
      class="d-table-row"
    >
      <IndexCell :initCellWidth="25" class="d-table-cell">
        {{ row.number }}
      </IndexCell>

      <Cell
        v-for="(column, indexCell) in table.columns"
        :key="indexCell"
        :cell="table.cells[indexRow * table.columns.length + indexCell]"
        class="d-table-cell"
      ></Cell>
    </v-row>

    <v-row class="d-table-row">
      <AddRowCell class="d-table-cell" />
    </v-row>
  </v-container>
</template>

<script>
import DescriptionRow from "./DescriptionRow.vue";

import Cell from "./Cells/Cell.vue";
import IndexCell from "./Cells/IndexCell.vue";
import AddColumnCell from "./Cells/AddColumnCell.vue";
import AddRowCell from "./Cells/AddRowCell.vue";

export default {
  name: "Table",
  components: {
    DescriptionRow,
    Cell,
    IndexCell,
    AddColumnCell,
    AddRowCell,
  },
  data: () => {
    return {};
  },
  computed: {
    table() {
      return this.$store.getters.table;
    },
  },
  methods: {
    test: () => {
      console.log("test ok");
    },
  },
};
</script>

<style>
</style>