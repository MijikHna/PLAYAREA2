<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-undo</v-icon>
      </v-btn>
    </template>
    <span>Undo</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "UndoButton",
};
</script>

<style></style>