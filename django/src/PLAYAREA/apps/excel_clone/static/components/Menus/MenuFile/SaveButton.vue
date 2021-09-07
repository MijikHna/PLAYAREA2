<template>
  <div>
    <v-list-item link>
      <v-list-item-title @click="openModal">{{
        djangoTrans.btnName
      }}</v-list-item-title>
    </v-list-item>
    <div ref="modal-title" v-show="showModalContent">
      <div class="text-h4">{{ djangoTrans.headerName }}</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ExcelCloneEventBus from "../../../js/excelClone-EventBus.js";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  name: "SaveButton",
  data: () => {
    return {
      showModalContent: false,

      djangoTrans: {
        btnName: gettext("Save"),
        headerName: gettext("Save Table"),
      },
    };
  },
  methods: {
    openModal() {
      // set Listeners for Yes/No Button on globalBus
      ExcelCloneEventBus.$on("close", (confirmed) => {
        if (confirmed) {
          this.saveTable();
        }

        ExcelCloneEventBus.$off("close");

        globalModalElem.$refs["modal-simple-title"].children[0].remove();
        globalModalElem.currentComponent = "";
      });

      const globalModalElem =
        globalThis.excelClone.$children[0].$refs["modal-simple"];

      // show Modal and Header
      globalModalElem.showDialog = true;
      this.showModalContent = true;

      // set Header of Modal
      globalModalElem.$refs["modal-simple-title"].append(
        this.$refs["modal-title"]
      );
      globalModalElem.currentComponent = "SaveTable";
    },
    async saveTable() {
      // copy table
      const table = JSON.parse(JSON.stringify(this.$store.getters.table));

      // delete mode (not needed in DB)
      table.cells.forEach((cell) => {
        delete cell.mode;
      });

      let response = null;
      try {
        response = await axios({
          method: "put",
          url: `/apps/excel-clone/save/${table.id}/`,
          data: table,
        });
      } catch (e) {
        globalThis.notifier.$children[0].$refs.notifierWrapper.addNotifier(
          "Excel Clone",
          `${gettext(this.djangoTrans.headerName)}: ${e.message}`,
          e.name.toLowerCase()
        );
        return;
      }

      if (response.status === 201) {
        globalThis.notifier.$children[0].$refs.notifierWrapper.addNotifier(
          "Excel Clone",
          `${gettext(this.djangoTrans.headerName)}: ${response.data.message}`,
          "success"
        );
      }
    },
  },
};
</script>

<style>
</style>