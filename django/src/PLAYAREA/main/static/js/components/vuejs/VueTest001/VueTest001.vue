<template>
  <div class="mt-3">
    <AirportCards1 />
    <airport-cards1 />

    <hr class="rounded mx-3" />
    <AirportCards2 :airports="euAirports" />

    <airport-cards-2 :airports="usAirports" />

    <hr class="rounded mx-3" />

    <AirportCards3 :airports="euAirports" />
    <airport-cards-3 :airports="usAirports" />
    <!-- man kann die Card auch so benutzen-->
    <Card class="mx-5">
      <p>US Airport</p>
      <p>Total: {{ usAirports.length }}</p>
    </Card>
    <Card class="mx-5">
      <p>EU Airport</p>
      <p>Total: {{ euAirports.length }}</p>
    </Card>
  </div>
</template>

<script>
import AirportCards1 from "./AirportCards1.vue";
import AirportCards2 from "./AirportCards2.vue";
import AirportCards3 from "./AirportCards3.vue";
import Card from "./Card";

import usAirportsData from "./us-airports.js";
import euAirportsData from "./eu-airports.js";

export default {
  name: "VueTest001",
  components: {
    AirportCards1,
    AirportCards2,
    AirportCards3,
    Card,
  },
  data: function () {
    return {
      usAirports: usAirportsData,
      euAirports: euAirportsData,
    };
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

hr.rounded {
  border-top: 8px solid #bbb;
  border-radius: 5px;
}
</style>