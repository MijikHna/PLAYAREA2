<template>
  <v-container fluid>
    <DescriptionRow :columns="table.columns"></DescriptionRow>

    <v-row v-for="(row, indexRow) in table.rows" :key="indexRow">
      <IndexCell :initCellWidth="25">
        {{ row.number }}
      </IndexCell>

      <Cell
        v-for="(column, indexCell) in table.columns"
        :key="indexCell"
        :cell="table.cells[indexRow * table.columns.length + indexCell]"
      ></Cell>
    </v-row>

    <v-row>
      <AddRowCell />
    </v-row>
  </v-container>
</template>

<script>
import DescriptionRow from "./DescriptionRow.vue";

import Cell from "./Cells/Cell.vue";
import IndexCell from "./Cells/IndexCell.vue";
import AddColumnCell from "./Cells/AddColumnCell.vue";
import AddRowCell from "./Cells/AddRowCell.vue";

import table from "../fakeTable.js";

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
    return {
      table: table,
    };
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