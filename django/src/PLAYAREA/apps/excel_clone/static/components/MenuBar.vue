<template>
  <v-row justify="start" class="mx-3 my-1">
    <MenuFile></MenuFile>
    <MenuEdit></MenuEdit>
    <MenuView></MenuView>
    <MenuInsert></MenuInsert>
    <MenuFormat></MenuFormat>
    <MenuHelp></MenuHelp>
  </v-row>
</template>

<script>
import MenuFile from "./Menus/MenuFile.vue";
import MenuEdit from "./Menus/MenuEdit.vue";
import MenuView from "./Menus/MenuView.vue";
import MenuInsert from "./Menus/MenuInsert.vue";
import MenuFormat from "./Menus/MenuFormat.vue";
import MenuHelp from "./Menus/MenuHelp.vue";

export default {
  name: "MenuBar",
  components: {
    MenuFile,
    MenuEdit,
    MenuView,
    MenuInsert,
    MenuFormat,
    MenuHelp,
  },
  data: () => {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
</style>