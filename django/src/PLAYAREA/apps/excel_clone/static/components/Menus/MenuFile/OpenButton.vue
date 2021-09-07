<template>
  <div>
    <v-list-item link>
      <v-list-item-title @click="getTables">{{
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
  name: "OpenButton",
  data: () => {
    return {
      selectedTableId: null,
      showModalContent: false,

      djangoTrans: {
        btnName: gettext("Open"),
        headerName: gettext("Open table"),
      },
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
        ExcelCloneEventBus.$on("close", (data) => {
          if (data) {
            this.openTable();
          }
          ExcelCloneEventBus.$off("close");

          globalModalElem.$refs["modal-simple-title"].children[0].remove();
          globalModalElem.currentComponent = "";
          globalModalElem.currentComponentProps = null;
        });

        ExcelCloneEventBus.$on("selectedTableName", (data) => {
          this.selectedTableId = data;
        });

        const globalModalElem =
          globalThis.excelClone.$children[0].$refs["modal-simple"];

        globalModalElem.showDialog = true;
        this.showModalContent = true;

        globalModalElem.$refs["modal-simple-title"].append(
          this.$refs["modal-title"]
        );
        globalModalElem.currentComponent = "OpenTable";
        globalModalElem.currentComponentProps = {
          tables: response.data,
        };
      }
    },
    async openTable() {
      window.location.href = `/apps/excel-clone/${this.selectedTableId}`;

      this.selectedTableId = null;
    },
  },
};
</script>

<style>
</style>