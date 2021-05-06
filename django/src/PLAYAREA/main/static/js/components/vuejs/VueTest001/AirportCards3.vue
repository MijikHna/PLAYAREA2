<template>
  <div class="wrapper">
    <Card v-for="airport in airports" :key="airport.abbreviation">
      <p>{{ airport.abbreviation }}</p>
      <p>{{ airport.name }}</p>
      <p>{{ airport.city }}, {{ airport.state }}</p>
    </Card>
  </div>
</template>

<script>
import Card from "./Card";

export default {
  components: {
    Card,
  },
  name: "AirportCards3",
  props: {
    airports: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
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