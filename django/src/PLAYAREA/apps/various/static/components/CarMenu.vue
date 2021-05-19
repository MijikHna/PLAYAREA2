<template>
  <div class="container mt-3">
    <Car v-for="car in cars" :key="car.id" :carId="car.id"></Car>
    <Car :carId="0" />
  </div>
</template>

<script>
import axios from "axios";
import config from "../js/config.js";
import Car from "./Car.vue";
export default {
  name: "CarMenu",
  components: { Car },
  data() {
    return {
      cars: null,
      ...config,
    };
  },
  mounted() {
    this.getAllCars();
  },
  methods: {
    async getAllCars() {
      const response = await axios({
        method: "get",
        url: this.config.urls.allCars,
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.status === 200) {
        console.log(response.data);
        this.cars = response.data;
      }
    },
  },
};
</script>

<style></style>