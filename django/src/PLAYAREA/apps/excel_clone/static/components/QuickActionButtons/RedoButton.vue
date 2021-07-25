<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-redo</v-icon>
      </v-btn>
    </template>
    <span>Redo</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "RedoButton",
};
</script>

<style></style>