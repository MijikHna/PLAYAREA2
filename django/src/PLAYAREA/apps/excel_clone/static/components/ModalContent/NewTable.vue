<template>
  <v-text-field
    v-model="tableName"
    :rules="rules"
    counter="25"
    :hint="djangoTrans.hint"
    :label="djangoTrans.label"
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
      djangoTrans: {
        hint: gettext("Enter the name of the new table"),
        label: gettext("Table name"),
      },
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