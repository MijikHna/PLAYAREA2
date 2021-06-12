<template>
  <div
    ref="toast"
    class="toast fade hide min-width"
    role="alert"
    aria-live="assertive"
    aria-atomic="true"
    data-autohide="false"
  >
    <div class="toast-header">
      <svg class="rounded mr-2" width="20px" height="20px">
        <rect width="100%" height="100%" fill="#007aff"></rect>
      </svg>
      <strong class="mr-auto">
        <slot name="header"></slot>
      </strong>
      <small class="text-muted"> {{ elapsedTime }} </small>
      <button
        type="button"
        class="ml-2 mb-1 close"
        data-dismiss="toast"
        aria-label="Close"
        @click="closeToast"
      >
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div
      class="toast-body alert rounded-0 mb-0"
      :class="[
        result === 'error' ? 'alert-danger' : '',
        result === 'success' ? 'alert-success' : '',
      ]"
    >
      <slot name="body"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Notifier",
  data() {
    return {
      activatedTime: null,
      elapsedTime: null,
      timeOut: null,
    };
  },
  props: {
    result: String,
  },
  mounted() {
    $(this.$refs.toast).toast("show");
    this.activatedTime = new Date();
    this.calcTime();
  },
  methods: {
    calcTime() {
      //in millisec
      let currentTime = new Date();
      let diff = currentTime.getTime() - this.activatedTime.getTime();

      diff /= 1000;

      if (diff < 10) {
        this.elapsedTime = "just now";
      } else if (diff < 60) {
        diff = Math.round(diff);
        this.elapsedTime = `${diff} seconds ago`;
      } else {
        diff /= 60;
        if (diff < 10) {
          $(this.$refs.toast).toast("show");
        } else {
          $(this.$refs.toast).toast("hide");
          clearTimeout(this.timeOut);
          this.$emit("closeMe", this.$vnode.key);
          return;
        }
      }

      var options = {
        weekday: "long",
        year: "numeric",
        month: "numeric",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
      };

      console.log(this.activatedTime.toLocaleDateString("en-US", options));
      console.log(currentTime.toLocaleDateString("en-US", options));
      console.log(diff);
      // do recalc every minute
      this.timeOut = setTimeout(this.calcTime, 10000);
    },
    closeToast() {
      $(this.$refs.toast).toast("hide");
      clearTimeout(this.timeOut);
      this.$emit("closeMe", this.$vnode.key);
    },
  },
};
</script>

<style>
.min-width {
  min-width: 255px;
}
</style>