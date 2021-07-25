<template>
  <v-list-item link>
    <v-list-item-title>{{ btnName }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  name: "DeleteButton",
  data: () => {
    return {
      btnName: "Delete",
    };
  },
};
</script>

<style></style>