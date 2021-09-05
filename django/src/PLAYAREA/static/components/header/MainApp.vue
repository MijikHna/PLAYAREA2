<template>
  <li class="nav-item dropdown">
    <a
      :id="`navbar${app.name_stringified}Dropdown`"
      :class="classObj"
      href="#"
      role="button"
      data-toggle="dropdown"
      aria-haspopup="true"
      aria-expanded="false"
    >
      {{ app.name }}
    </a>
    <div class="dropdown-menu bg-primary">
      <template v-for="(subApp, index) in app.subApps">
        <SubApp :key="index" :app="subApp" :mainAppHref="app.href" />
      </template>
    </div>
  </li>
</template>

<script>
import SubApp from "./SubApp.vue";
export default {
  name: "MainApp",
  components: { SubApp },
  data() {
    return {
      classObj: "nav-link dropdown-toggle text-white",
    };
  },
  props: {
    app: Object,
  },
};
</script>

<style></style>