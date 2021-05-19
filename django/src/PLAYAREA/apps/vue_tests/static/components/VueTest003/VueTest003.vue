<template>
  <div id="app">
    <div class="container mt-3 mx-2">
      <div class="row">
        <Button class="mx-2" :onClick="consoleClick">My Test</Button>
        <Button class="mx-2" :onClick="alertClick" disabled>
          <i class="fa fas-close"></i>
        </Button>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "./Button";
export default {
  name: "VueTest003",
  components: { Button },
  methods: {
    consoleClick() {
      console.log("Button clicked");
    },
    alertClick() {
      alert("Button clicked");
    },
  },
};
</script>

<style>
</style>