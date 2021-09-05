<template>
  <div
    v-if="show"
    class="full-screen d-flex justify-center align-center amber lighten-4 ma-5"
  >
    <div>
      <v-progress-circular
        :size="100"
        color="green"
        indeterminate
        class="m-auto d-block"
      ></v-progress-circular>
      <div>{{ dialogText }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProgressFullScreen",
  data: () => {
    return {
      dialogText: null,
      show: false,
    };
  },
  methods: {
    showProgress(dialogText = null) {
      this.dialogText = dialogText;
      this.show = true;
    },
    hideProgress() {
      this.dialogText = null;
      this.show = false;
    },
  },
};
</script>

<style scoped>
.full-screen {
  position: fixed;
  top: -10px;
  left: -10px;
  z-index: 1000;
  height: calc(100% - 20px);
  width: calc(100% - 20px);
  opacity: 0.85;
}
</style>