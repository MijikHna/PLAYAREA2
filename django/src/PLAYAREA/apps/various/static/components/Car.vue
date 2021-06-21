<template>
  <div class="container">
    <div class="row mb-2 justify-content-around">
      <button class="btn btn-primary mx-2" @click="getCar">GET</button>
      <button class="btn btn-primary mx-2" @click="createCar">POST</button>
      <button class="btn btn-primary mx-2">PUT</button>
      <button class="btn btn-primary mx-2">DELETE</button>
    </div>
    <div v-if="showCarInput" class="row mb-4 mx-2 border rounded">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text" id="">{{ carId }}</span>
        </div>
        <input
          v-model="carName"
          type="text"
          name="car-name"
          id="car-name"
          class="form-control"
        />
        <input
          v-model="carModel"
          type="text"
          name="car-model"
          id="car-model"
          class="form-control"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { config } from "../js/config.js";
export default {
  name: "Car",
  data() {
    return {
      showCarInput: false,
      carName: null,
      carModel: null,
      config: config,
    };
  },
  props: {
    carId: Number,
  },
  methods: {
    async getCar() {
      if (!this.showCarInput && this.carId > 0) {
        const response = await axios({
          method: "get",
          url: `${this.config.urls.getCar}/${this.carId}`,
        });

        if (response.status === 200) {
          console.log(response.data);
          this.carId = response.data.id;
          this.carName = response.data.name;
          this.carModel = response.data.model;
          this.showCarInput = true;
        }

        return;
      }

      this.showCarInput = false;
    },
    async createCar() {
      const csrfToken = await window.cookieStore.get("csrftoken");
      if (this.showCarInput && this.carId <= 0) {
        const response = await axios({
          method: "post",
          url: `${this.config.urls.createCar}/`,
          data: {
            name: this.carName,
            model: this.carModel,
          },
          headers: {
            "X-CSRFToken": csrfToken.value,
          },
        });

        if (response.status === 201) {
          //console.log(response.data);
          location.reload();
        }
        return;
      }

      this.showCarInput = true;
    },
    async changeCar() {},
    async deleteCar() {},
  },
};
</script>

<style>
</style>