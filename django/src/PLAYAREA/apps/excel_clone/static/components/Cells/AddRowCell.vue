<template>
  <v-sheet
    color="grey lighten-1"
    elevation="1"
    :max-height="cellHeight - 1"
    :max-width="cellWidth - 1"
  >
    <div class="">
      <slot>
        <v-tooltip bottom>
          <template v-slot:activator="{ attrs, on }">
            <span v-bind="attrs" v-on="on" class="align-center justify-center">
              <v-icon>mdi-plus-box</v-icon>
            </span>
          </template>
          <span>{{ djangoTrans.tooltip }}</span>
        </v-tooltip>
      </slot>
    </div>
  </v-sheet>
</template>

<script>
export default {
  name: "AddRowCell",
  data: () => {
    return {
      cellHeight: 25,
      cellWidth: 25,
      djangoTrans: {
        tooltip: gettext("Add new row"),
      },
    };
  },
};
</script>

<style></style>