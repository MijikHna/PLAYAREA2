<template>
  <div>{{ djangoTrans.confText }}</div>
</template>

<script>
export default {
  name: "SaveTable",
  data: () => {
    return {
      djangoTrans: {
        confText: gettext("Do you really want to save Table?"),
      },
    };
  },
};
</script>

<style>
</style>