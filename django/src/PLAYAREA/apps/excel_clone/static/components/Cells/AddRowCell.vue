<template>
  <v-sheet
    color="grey lighten-1"
    elevation="1"
    :height="cellHeight"
    :width="cellWidth"
  >
    <div class="d-flex border">
      <slot>
        <v-tooltip bottom>
          <template v-slot:activator="{ attrs, on }">
            <v-btn
              icon
              small
              tile
              v-bind="attrs"
              v-on="on"
              :width="cellWidth - 1"
              :height="cellHeight - 1"
              class="align-center justify-center"
            >
              <v-icon>mdi-plus-box</v-icon>
            </v-btn>
          </template>
          <span>Add new row</span>
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
    };
  },
};
</script>

<style>
</style>