<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-format-color-text</v-icon>
      </v-btn>
    </template>
    <span>Text color</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "TextColorButton",
};
</script>

<style></style>