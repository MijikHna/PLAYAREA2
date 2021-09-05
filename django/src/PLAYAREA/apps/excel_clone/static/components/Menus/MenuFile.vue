<template>
  <v-menu
    :rounded="'0'"
    transition="scale-transition"
    offset-y
    :close-on-click="closeOnClick"
  >
    <template v-slot:activator="{ attrs, on }">
      <v-btn v-bind="attrs" v-on="on" elevation="2" text small tile outlined>
        {{ djangoTrans.btnName }}
      </v-btn>
    </template>

    <v-list>
      <NewButton></NewButton>
      <OpenButton></OpenButton>
      <SaveButton></SaveButton>
      <DeleteButton></DeleteButton>
      <CloseButton></CloseButton>
    </v-list>
  </v-menu>
</template>

<script>
import NewButton from "./MenuFile/NewButton.vue";
import OpenButton from "./MenuFile/OpenButton.vue";
import SaveButton from "./MenuFile/SaveButton.vue";
import DeleteButton from "./MenuFile/DeleteButton.vue";
import CloseButton from "./MenuFile/CloseButton.vue";
export default {
  name: "MenuFile",
  components: { NewButton, OpenButton, SaveButton, DeleteButton, CloseButton },
  data: () => {
    return {
      closeOnClick: true,
      djangoTrans: {
        btnName: gettext("File"),
      },
    };
  },
  methods: {},
};
</script>

<style scoped></style>