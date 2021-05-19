<template>
  <div id="app">
    <div class="wrapper">
      <div v-for="airport in airports" :key="airport.abbreviation" class="card">
        <p>{{ airport.abbreviation }}</p>
        <p>{{ airport.name }}</p>
        <p>{{ airport.city }}, {{ airport.state }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import data from "./us-airports.js";
export default {
  name: "VueTest001",
  data: function () {
    return { airports: data };
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
.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-column-gap: 1rem;
  max-width: 960px;
  margin: 0 auto;
}

.card {
  border: 3px solid;
  border-radius: 0.5rem;
  padding: 1rem;
  margin-bottom: 1rem;
}

.card p:first-child {
  font-weight: bold;
  font-size: 2.5rem;
  margin: 1rem 0;
}

.card p:last-child {
  font-style: italic;
  font-size: 0.8rem;
}
</style>