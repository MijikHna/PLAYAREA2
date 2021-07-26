<template>
  <div>
    <v-list-item link>
      <v-list-item-title @click="getTables">{{ btnName }}</v-list-item-title>
    </v-list-item>

    <div ref="modal-title" v-show="showModalContent">
      <div class="text-h4">Open table</div>
    </div>
    <div ref="modal-body" v-show="showModalContent">
      <v-select
        v-model="selectedTable"
        :hint="'Choose a table'"
        :items="tables"
        item-text="tableName"
        item-value="id"
        label="Choose a table"
      ></v-select>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ExcelCloneEventBus from "../../../js/excelClone-EventBus.js";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  name: "OpenButton",
  data: () => {
    return {
      selectedTable: null,
      tables: [],
      btnName: "Open",
      showModalContent: false,
      rules: [(v) => v.length <= 25 || "Max 25 characters"],
    };
  },
  methods: {
    async getTables() {
      let response = null;
      try {
        response = await axios({
          method: "get",
          url: `/apps/excel-clone/get-tables/`,
        });
      } catch (e) {
        globalThis.notifier.$children[0].$refs.notifierWrapper.addNotifier(
          "Excel Clone",
          `Open table: ${e.message}`,
          e.name.toLowerCase()
        );
      }

      if (response.status === 200) {
        this.tables = response.data;

        const globalModalElem =
          globalThis.excelClone.$children[0].$refs["modal-simple"];
        globalModalElem.$refs["modal-simple-title"].append(
          this.$refs["modal-title"]
        );
        globalModalElem.$refs["modal-simple-body"].append(
          this.$refs["modal-body"]
        );

        ExcelCloneEventBus.$on("close", (data) => {
          if (data) {
            this.openTable();
          }
          ExcelCloneEventBus.$off("close");
          globalModalElem.$refs["modal-simple-title"].children[0].remove();
          globalModalElem.$refs["modal-simple-body"].children[0].remove();

          this.tableName = "";
        });

        globalModalElem.showDialog = true;
        this.showModalContent = true;
      }
    },
    async openTable() {
      let response = null;
      try {
        response = await axios({
          method: "get",
          url: `/apps/excel-clone/open/${this.selectedTable}`,
        });
      } catch (e) {
        globalThis.notifier.$children[0].$refs.notifierWrapper.addNotifier(
          "Excel Clone",
          `Open table: ${e.message}`,
          e.name.toLowerCase()
        );

        this.$store.commit("setTable", null);

        return;
      }

      if (response.status === 200) {
        this.$store.commit("setTable", response.data);
      }

      this.tableName = "";
    },
    clearInput() {
      this.tableName = "";
    },
  },
};
</script>

<style>
</style>