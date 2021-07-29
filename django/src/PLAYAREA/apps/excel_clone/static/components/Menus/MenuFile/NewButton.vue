<template>
  <div>
    <v-list-item link>
      <v-list-item-title @click="openModal">{{ btnName }}</v-list-item-title>
    </v-list-item>

    <div ref="modal-title" v-show="showModalContent">
      <div class="text-h4">Table name</div>
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
      btnName: "New",
      tableName: null,

      showModalContent: false,
    };
  },
  methods: {
    openModal() {
      ExcelCloneEventBus.$on("close", (data) => {
        if (data) {
          this.createNewTable();
        }
        ExcelCloneEventBus.$off("close");
        ExcelCloneEventBus.$off("choosenTableName");

        this.tableName = "";
        this.showModalContent = false;

        globalModalElem.$refs["modal-simple-title"].children[0].remove();
        globalModalElem.currentComponent = "";
      });

      ExcelCloneEventBus.$on("choosenTableName", (data) => {
        this.tableName = data;
      });

      const globalModalElem =
        globalThis.excelClone.$children[0].$refs["modal-simple"];

      globalModalElem.showDialog = true;
      this.showModalContent = true;

      globalModalElem.$refs["modal-simple-title"].append(
        this.$refs["modal-title"]
      );
      globalModalElem.currentComponent = "NewTable";
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
    },
  },
};
</script>

<style>
</style>