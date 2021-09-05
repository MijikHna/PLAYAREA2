<template>
  <v-sheet
    color="grey lighten-1"
    elevation="1"
    :max-height="cellHeight"
    :min-width="cellWidth"
  >
    <div class="border border-left-0 m-auto text-center">
      {{ content }}
    </div>
  </v-sheet>
</template>

<script>
export default {
  name: "IndexCell",
  data: () => {
    return {
      cellHeight: null,
      cellWidth: null,
    };
  },
  props: {
    initCellWidth: {
      Type: Number,
      required: true,
    },
    initCellHeight: {
      type: Number,
      required: true,
    },
    content: {
      type: String | Number,
      default: "\xa0",
    },
    columns: {
      type: Array,
      default: null,
    },
    row: {
      type: Array,
      default: null,
    },
  },
  mounted() {
    this.cellWidth = this.initCellWidth;
    this.cellHeight = this.initCellHeight;
  },
};
</script>

<style>
</style>