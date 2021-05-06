<template>
  <div class="m-2 border-top" v-show="isActive">
    <slot />
  </div>
</template>

<script>
export default {
  name: "Tab",
  props: {
    title: {
      type: String,
      default: "Tab",
    },
  },
  data() {
    return {
      isActive: true,
    };
  },
};
</script>

<style>
</style>