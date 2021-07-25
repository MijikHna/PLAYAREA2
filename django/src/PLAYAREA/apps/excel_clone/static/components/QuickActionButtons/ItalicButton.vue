<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-format-italic</v-icon>
      </v-btn>
    </template>
    <span>Italic</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "ItalicButton",
};
</script>

<style></style>