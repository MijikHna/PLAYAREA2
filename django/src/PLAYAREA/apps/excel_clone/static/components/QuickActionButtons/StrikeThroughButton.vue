<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-format-strikethrough</v-icon>
      </v-btn>
    </template>
    <span>Strike through</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "StirkeThroughButton",
};
</script>

<style></style>