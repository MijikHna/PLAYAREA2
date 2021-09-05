<template>
  <v-list-item link>
    <v-list-item-title>{{ djangoTrans.btnName }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  name: "SaveButton",
  data: () => {
    return {
      djangoTrans: {
        btnName: gettext("Save"),
      },
    };
  },
};
</script>

<style>
</style>