<template>
  <v-app>
    <v-container fluid>
      <v-row justify="center">
        <div class="h4">Excel Clone</div>
      </v-row>

      <v-row justify="start">
        <v-menu
          v-for="btn in btns"
          :key="btn"
          :rounded="true"
          transition="scale-transition"
          offset-y
        >
          <template v-slot:activator="{ attrs, on }">
            <v-btn v-bind="attrs" v-on="on" elevation="2" text small tile>
              {{ btn }}
            </v-btn>
          </template>

          <v-list>
            <v-list-item v-for="item in items" :key="item" link>
              <v-list-item-title v-text="item"></v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-row>

      <v-row justify="start">
        <v-menu
          v-for="btn in btns"
          :key="btn"
          :rounded="true"
          transition="scale-transition"
          offset-y
        >
          <template v-slot:activator="{ attrs, on }">
            <!-- <MenuButton v-bind="attrs" v-on:click.native="click" v-bind:on="on"> -->
            <MenuButton v-bind="attrs" v-on="on">
              <template v-slot:default="{ test }">
                {{ btn }} {{ test.firstName }}
              </template>
            </MenuButton>
          </template>
          <v-list>
            <v-list-item v-for="item in items" :key="item" link>
              <v-list-item-title v-text="item"></v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-row>
      <Table />
    </v-container>
  </v-app>
</template>

<script>
import Table from "../Table.vue";
import MenuButton from "./MenuButton.vue";
import Button from "../../../../vue_tests/static/components/VueTest003/Button.vue";

export default {
  name: "Menu",
  components: { Table, MenuButton, Button },
  data: () => {
    return {
      btns: ["File", "Edit", "View", "Insert", "Format", "Help"],
      btns2: [
        { text: "File", showMenu: false },
        { text: "Edit", showMenu: false },
      ],
      items: ["test1", "test2"],
      x: 0,
      y: 0,
      test: null,
    };
  },
  methods: {
    show(index, e) {
      e.preventDefault();
      this.btns2[index].showMenu = false;
      this.x = e.clientX;
      this.y = e.clientY;
      this.$nextTick(() => {
        this.btns2[index].showMenu = true;
      });
    },
    testFunk() {
      console.log(test);
    },
  },
};
</script>

<style scoped>
::v-deep .v-application--wrap {
  min-height: calc(100vh - 56px);
  min-height: -webkit-fill-available; /* mobile viewport bug fix */
}
</style>