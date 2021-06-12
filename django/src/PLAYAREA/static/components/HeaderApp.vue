<template>
  <a :href="'/apps/' + appHref" :class="appClass">
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
      appHref: null,
      appClass: null,
    };
  },
  beforeMount() {
    this.appName = this.$parent.$el.getAttribute("data-name");
    this.appStringified = this.$parent.$el.getAttribute("data-stringified");
    this.appHref = this.$parent.$el.getAttribute("data-href");
    this.appClass = this.$parent.$el.getAttribute("data-class");
  },
};
</script>

<style></style>