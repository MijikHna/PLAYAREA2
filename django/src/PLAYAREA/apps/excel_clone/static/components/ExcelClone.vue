<template>
  <v-app>
    <v-container fluid class="px-0">
      <v-row justify="center">
        <div class="h4">{{ djangoTrans.tableHeader }} {{ tableName }}</div>
      </v-row>

      <MenuBar></MenuBar>
      <v-divider class="mt-2 mb-0" />

      <QuickActionBar></QuickActionBar>
      <v-divider class="mt-0 mb-0" />

      <Table ref="excel-table"></Table>

      <ContextMenu ref="context-menu" />
      <ModalSimple ref="modal-simple" />
      <ProgressFullScreen ref="progress-fullscreen" />
    </v-container>
  </v-app>
</template>

<script>
import MenuBar from "./MenuBar.vue";
import QuickActionBar from "./QuickActionBar.vue";
import Table from "./Table.vue";

import ContextMenu from "./ContextMenu.vue";
import ModalSimple from "./ModalSimple.vue";
import ProgressFullScreen from "./ProgressFullScreen.vue";
export default {
  name: "ExcelClone",
  components: {
    MenuBar,
    QuickActionBar,
    Table,
    ContextMenu,
    ModalSimple,
    ProgressFullScreen,
  },
  data: () => {
    return {
      djangoTrans: {
        tableHeader: gettext("Excel Clone:"),
      },
    };
  },
  computed: {
    tableName() {
      return this.$store.getters.tableName;
    },
  },
};
</script>

<style scoped>
::v-deep .v-application--wrap {
  min-height: -webkit-fill-available; /* mobile viewport bug fix */
  min-height: calc(100vh - 56px);
}
</style>