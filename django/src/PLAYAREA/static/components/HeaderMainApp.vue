<template>
  <a
    :id="appId"
    :class="appClass"
    href="#"
    role="button"
    data-toggle="dropdown"
    aria-haspopup="true"
    aria-expanded="false"
  >
    {{ appName }}
  </a>
</template>

<script>
export default {
  name: "HeaderApp",
  data() {
    return {
      appName: null,
      appStringified: null,
      appClass: null,
      appSubApps: false,
      appId: null,
    };
  },
  beforeMount() {
    this.appName = this.$parent.$el.getAttribute("data-name");
    this.appStringified = this.$parent.$el.getAttribute("data-stringified");
    this.appClass = this.$parent.$el.getAttribute("data-class");
    this.appSubApps = this.$parent.$el.getAttribute("data-subapps");
    this.appId = this.$parent.$el.getAttribute("data-id");
  },
};
</script>

<style></style>