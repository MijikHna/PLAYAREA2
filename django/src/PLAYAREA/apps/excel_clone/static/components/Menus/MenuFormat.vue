<template>
  <v-menu
    :rounded="'0'"
    transition="scale-transition"
    offset-y
    :close-on-click="closeOnClick"
  >
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
  name: "MenuFormat",
  components: {},
  data: () => {
    return {
      btnName: "Format",
      closeOnClick: true,
    };
  },
  methods: {},
};
</script>

<style scoped></style>