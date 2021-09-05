<template>
  <v-select
    v-model="selectedTable"
    :hint="djangoTrans.hint"
    :items="tables"
    item-text="tableName"
    item-value="id"
    :label="djangoTrans.label"
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
      djangoTrans: {
        hint: gettext("Choose a table"),
        label: gettext("Choose a table"),
      },
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