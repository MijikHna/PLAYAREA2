<template>
  <a :href="'/apps/' + mainAppHref + app.href" :class="classObj">
    {{ app.name }}
  </a>
</template>

<script>
export default {
  name: "SubApp",
  data() {
    return {
      classObj: "dropdown-item text-white",
    };
  },
  props: {
    app: Object,
    mainAppHref: String,
  },
};
</script>

<style></style>