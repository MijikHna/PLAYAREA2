<template>
  <div class="container mt-3">
    <div class="row p-4 border border-info">
      <div class="col mx-2 my-auto" v-for="app in apps" :key="app.id">
        <!-- bei :destination ternary benutzen -->
        <AppCard
          class=""
          :cardHeader="app.name"
          :cardTitle="app.name"
          :cardText="app.name"
          :cardButtonText="app.name"
          :destination="app.href"
          :subApps="app.subApps"
        >
        </AppCard>
      </div>
    </div>
  </div>
</template>

<script>
import config from "../js/config.js";
import AppCard from "./AppCard.vue";
export default {
  name: "Apps",
  components: { AppCard },
  data: function () {
    return {
      apps: null,
      ...config,
    };
  },
  mounted() {
    this.getAllApps();
  },
  methods: {
    getAllApps: async function () {
      const response = await fetch(this.config.urls.allApps, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.status === 200) {
        const data = await response.json();
        if (data) {
          /*
          this.apps = data.map((app) => {
            if (!app.href.startsWith("/")) {
              app.href = "/" + app.href;
            }
            return app;
          });
          */
          this.apps = data;
          console.log(data);
        }
      }
    },
  },
};
</script>

<style></style>