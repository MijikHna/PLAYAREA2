<template>
  <li class="nav-item">
    <a :href="'/apps/' + app.href" :class="classObj">
      {{ app.name }}
    </a>
  </li>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      classObj: "nav-link text-white",
    };
  },
  props: {
    app: Object,
  },
};
</script>

<style></style>