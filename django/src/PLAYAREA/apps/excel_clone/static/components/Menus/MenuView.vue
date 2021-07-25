<template>
  <v-menu :rounded="'0'" transition="scale-transition" offset-y>
    <template v-slot:activator="{ attrs, on }">
      <v-btn v-bind="attrs" v-on="on" elevation="2" text small tile outlined>
        {{ btnName }}
      </v-btn>
    </template>

    <v-list> </v-list>
  </v-menu>
</template>

<script>
export default {
  name: "MenuView",
  components: {},
  data: () => {
    return {
      btnName: "View",
    };
  },
  methods: {},
};
</script>

<style scoped></style>