<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-undo</v-icon>
      </v-btn>
    </template>
    <span>{{ djangoTrans.tooltip }}</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "UndoButton",
  data: () => {
    return {
      djangoTrans: {
        tooltip: gettext("Undo"),
      },
    };
  },
};
</script>

<style></style>