<template>
  <div>
    <v-list-item link>
      <v-list-item-title @click="askTableName">{{ btnName }}</v-list-item-title>
    </v-list-item>

    <div ref="modal-title" v-show="showModalContent">
      <div class="text-h4">Table name</div>
    </div>
    <div ref="modal-body" v-show="showModalContent">
      <v-text-field
        v-model="tableName"
        :rules="rules"
        counter="25"
        hint="Enter the name of the new table"
        label="Table name"
      >
      </v-text-field>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ExcelCloneEventBus from "../../../js/excelClone-EventBus.js";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  name: "NewButton",
  data: () => {
    return {
      tableName: "",
      btnName: "New",
      showModalContent: false,
      rules: [(v) => v.length <= 25 || "Max 25 characters"],
    };
  },
  methods: {
    askTableName() {
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
          this.createNewTable();
        }
        ExcelCloneEventBus.$off("close");

        globalModalElem.$refs["modal-simple-title"].children[0].remove();
        globalModalElem.$refs["modal-simple-body"].children[0].remove();

        this.tableName = "";
      });

      globalModalElem.showDialog = true;
      this.showModalContent = true;
    },
    async createNewTable() {
      let response = null;
      try {
        response = await axios({
          method: "post",
          url: `/apps/excel-clone/new/`,
          data: {
            tableName: this.tableName,
          },
        });
      } catch (e) {
        globalThis.notifier.$children[0].$refs.notifierWrapper.addNotifier(
          "Excel Clone",
          `Create New Table: ${e.message}`,
          e.name.toLowerCase()
        );

        this.$store.commit("setTable", null);

        return;
      }

      if (response.status === 201) {
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