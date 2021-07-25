<template>
  <v-sheet
    color="grey lighten-1"
    elevation="1"
    :height="cellHeight"
    :width="cellWidth"
  >
    <div class="border border-left-0 m-auto text-center">
      <slot></slot>
    </div>
  </v-sheet>
</template>

<script>
export default {
  name: "IndexCell",
  data: () => {
    return {
      cellHeight: 25,
      cellWidth: null,
    };
  },
  props: {
    initCellWidth: {
      Type: Number,
      required: true,
    },
  },
  mounted() {
    this.cellWidth = this.initCellWidth;
  },
};
</script>

<style>
</style>