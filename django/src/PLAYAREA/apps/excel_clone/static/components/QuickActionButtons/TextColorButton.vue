<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ attrs, on }">
      <v-btn icon small tile v-bind="attrs" v-on="on">
        <v-icon>mdi-format-color-text</v-icon>
      </v-btn>
    </template>
    <span>{{ djangoTrans.tooltip }}</span>
  </v-tooltip>
</template>

<script>
export default {
  name: "TextColorButton",
  data: () => {
    return {
      djangoTrans: {
        tooltip: gettext("Text color"),
      },
    };
  },
};
</script>

<style></style>