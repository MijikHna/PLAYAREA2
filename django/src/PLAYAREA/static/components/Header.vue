<template>
  <ul v-if="apps" class="navbar-nav mr-auto">
    <template v-for="(app, index) in apps">
      <App v-if="app.subApps.length == 0" :key="index" :app="app" />
      <MainApp v-else :key="index" :app="app" />
    </template>
    <li class="d-lg-none nav-item dropdown">
      <a
        class="nav-link dropdown-toggle text-white"
        href="#"
        id="UserSettingsDropdown"
        role="button"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
        >My Account</a
      >
      <div class="dropdown-menu bg-primary">
        <a class="dropdown-item text-white" href="/apps/accounts/dashboard"
          >My Profile</a
        >
        <a class="dropdown-item text-white" href="/apps/accounts/logout"
          >Logout</a
        >
      </div>
    </li>
  </ul>
</template>
<script>
import App from "./header/App.vue";
import MainApp from "./header/MainApp.vue";
export default {
  name: "Header",
  components: { App, MainApp },
  data: () => {
    return {
      apps: null,
    };
  },
  mounted() {
    this.apps = window.apps;
    // delete window.apps;
    // window.apps = undefined;
  },
};
</script>

<style>
</style>