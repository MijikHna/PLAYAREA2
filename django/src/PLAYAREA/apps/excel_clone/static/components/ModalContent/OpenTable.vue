<template>
  <v-select
    v-model="selectedTable"
    :hint="'Choose a table'"
    :items="tables"
    item-text="tableName"
    item-value="id"
    label="Choose a table"
    @input="transferSelectedTableName"
  ></v-select>
</template>

<script>
import ExcelCloneEventBus from "../../js/excelClone-EventBus";
export default {
  name: "OpenTable",
  data: () => {
    return {
      selectedTable: null,
    };
  },
  props: {
    tables: {
      type: Array,
      required: true,
    },
  },
  methods: {
    transferSelectedTableName() {
      ExcelCloneEventBus.$emit("selectedTableName", this.selectedTable);
    },
  },
};
</script>

<style></style>