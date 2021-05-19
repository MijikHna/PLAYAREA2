<template>
  <div class="mt-4">
    <div class="row">
      <div class="col text-center">
        <button class="btn btn-primary" @click="openModal1()">Test 001</button>
      </div>
      <Modal001 :open="showModal1" @done="showRecievedData1" />
    </div>
    <div class="row text-center">
      <div class="col">
        <p class="border border-info mx-5 mt-4" v-if="modalRecievedText1">
          {{ modalRecievedText1 }}
        </p>
      </div>
    </div>

    <hr class="rounded mx-3" />
    <div class="row">
      <div class="col text-center">
        <button class="btn btn-primary" @click="openModal2()">Test 002</button>
      </div>
      <Modal001 :open="showModal2" @done="showRecievedData2">
        <div class="text-primary">Moda 2</div>
      </Modal001>
    </div>
    <div class="row text-center">
      <div class="col">
        <p class="border border-info mx-5 mt-4" v-if="modalRecievedText2">
          {{ modalRecievedText2 }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Modal001 from "./Modal001";
export default {
  name: "VueTestModal001.vue",
  components: {
    Modal001,
  },
  data() {
    return {
      modalRecievedText1: null,
      modalRecievedText2: null,
      showModal1: false,
      showModal2: false,
    };
  },
  methods: {
    openModal1() {
      this.modalRecievedText1 = null;
      this.showModal1 = true;
    },
    openModal2() {
      this.modalRecievedText2 = null;
      this.showModal2 = true;
    },
    showRecievedData1(recievedData) {
      if (recievedData) {
        this.modalRecievedText1 = recievedData;
      }
      this.showModal1 = false;
    },
    showRecievedData2(recievedData) {
      if (recievedData) {
        this.modalRecievedText2 = recievedData;
      }
      this.showModal2 = false;
    },
  },
};
</script>

<style>
</style>