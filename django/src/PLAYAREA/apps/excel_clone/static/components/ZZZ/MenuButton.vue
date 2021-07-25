<template>
  <button class="menu-button" v-on="$listeners">
    <slot v-bind:test="test"></slot>
  </button>
</template>

<script>
export default {
  name: "MenuButton",
  data: () => {
    return {
      test: {
        firstName: "First",
        lastName: "Last",
      },
    };
  },
  mounted() {},
};
</script>

<style>
.menu-button {
}
</style>