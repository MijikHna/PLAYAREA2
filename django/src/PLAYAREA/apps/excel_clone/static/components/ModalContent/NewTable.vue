<template>
  <v-text-field
    v-model="tableName"
    :rules="rules"
    counter="25"
    hint="Enter the name of the new table"
    label="Table name"
    @input="choosenTableName"
  >
  </v-text-field>
</template>

<script>
import axios from "axios";
import ExcelCloneEventBus from "../../js/excelClone-EventBus";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  name: "NewTable",
  data: () => {
    return {
      tableName: "",
      rules: [(v) => v.length <= 25 || "Max 25 characters"],
    };
  },
  props: {
    tables: [],
  },
  methods: {
    choosenTableName() {
      ExcelCloneEventBus.$emit("choosenTableName", this.tableName);
    },
  },
};
</script>

<style></style>