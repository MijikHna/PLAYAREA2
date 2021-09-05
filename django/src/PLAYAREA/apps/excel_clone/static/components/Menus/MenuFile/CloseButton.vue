<template>
  <v-list-item link>
    <v-list-item-title>{{ djangoTrans.btnName }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  name: "CloseButton",
  data: () => {
    return {
      djangoTrans: {
        btnName: gettext("Close"),
      },
    };
  },
};
</script>

<style>
</style>