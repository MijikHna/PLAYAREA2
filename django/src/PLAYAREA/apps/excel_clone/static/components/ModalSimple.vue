<template>
  <v-dialog
    eager
    v-model="showDialog"
    width="600"
    class="text-center"
    @keydown.esc="decline"
    @click:outside="decline"
  >
    <v-card>
      <v-card-title class="text-h5 grey lighten-2">
        <div id="modal-simple-title" ref="modal-simple-title"></div>
        <slot name="modalTitle"></slot>
      </v-card-title>

      <v-card-text>
        <component
          :is="currentComponent"
          v-bind="currentComponentProps"
        ></component>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="confirm">
          {{ djangoTrans.confirm }}
        </v-btn>
        <v-btn color="primary" text @click="decline">
          {{ djangoTrans.decline }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import ExcelCloneEventBus from "../js/excelClone-EventBus.js";

export default {
  name: "ModalSimple",
  components: {
    "NewTable": () => import("./ModalContent/NewTable.vue"),
    "OpenTable": () => import("./ModalContent/OpenTable.vue"),
  },
  data: () => {
    return {
      showDialog: false,
      currentComponent: "",
      currentComponentProps: null,
      djangoTrans: {
        confirm: gettext("Confirm"),
        decline: gettext("Decline"),
      },
    };
  },
  methods: {
    decline() {
      this.showDialog = false;
      ExcelCloneEventBus.$emit("close", false);
    },
    confirm() {
      this.showDialog = false;
      ExcelCloneEventBus.$emit("close", true);
    },
  },
};
</script>

<style></style>