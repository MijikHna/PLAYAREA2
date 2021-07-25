<template>
  <v-dialog eager v-model="showDialog" width="600" class="text-center">
    <v-card>
      <v-card-title class="text-h5 grey lighten-2">
        <div id="modal-simple-title" ref="modal-simple-title">
          <slot name="title" ref="modal-title"></slot>
        </div>
      </v-card-title>

      <v-card-text>
        <div id="modal-simple-body" ref="modal-simple-body">
          <slot name="modalBody"></slot>
        </div>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="confirm"> Confirm </v-btn>
        <v-btn color="primary" text @click="decline"> Decline </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ModalSimple",
  data: () => {
    return {
      showDialog: false,
      confirmationFunction: null,
      declineFunction: null,
    };
  },
  props: {},
  methods: {
    decline() {
      this.showDialog = false;
      this.declineFunction();
      return false;
    },
    confirm() {
      this.showDialog = false;
      this.confirmationFunction();
      return true;
    },
  },
};
</script>

<style></style>