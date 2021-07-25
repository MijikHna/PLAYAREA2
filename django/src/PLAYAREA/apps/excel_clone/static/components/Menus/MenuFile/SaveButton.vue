<template>
  <v-list-item link>
    <v-list-item-title>{{ btnName }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  name: "SaveButton",
  data: () => {
    return {
      btnName: "Save",
    };
  },
};
</script>

<style>
</style>