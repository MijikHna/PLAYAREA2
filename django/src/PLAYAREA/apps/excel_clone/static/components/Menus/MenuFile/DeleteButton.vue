<template>
  <v-list-item link>
    <v-list-item-title>{{ djangoTrans.btnName }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  name: "DeleteButton",
  data: () => {
    return {
      djangoTrans: {
        btnName: gettext("Delete"),
      },
    };
  },
};
</script>

<style></style>