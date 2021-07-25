<template>
  <v-row>
    <IndexCell :cellDesc="''" :initCellWidth="25"></IndexCell>

    <IndexCell
      v-for="(column, index) in columns"
      :key="index"
      :cellDesc="column.notation"
      :initCellWidth="100"
    >
      {{ column.notation }}
    </IndexCell>

    <AddColumnCell />
  </v-row>
</template>

<script>
import IndexCell from "./Cells/IndexCell.vue";
import AddColumnCell from "./Cells/AddColumnCell.vue";

export default {
  name: "DescriptionRow",
  components: {
    IndexCell,
    AddColumnCell,
  },
  data: () => {
    return {};
  },
  props: {
    columns: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
</style>