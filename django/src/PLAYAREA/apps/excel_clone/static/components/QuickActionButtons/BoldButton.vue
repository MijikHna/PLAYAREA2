<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-format-bold</v-icon>
      </v-btn>
    </template>
    <span>Bold</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "BoldButton",
};
</script>

<style></style>