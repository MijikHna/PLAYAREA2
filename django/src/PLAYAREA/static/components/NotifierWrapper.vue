<template>
  <div id="notifier-wrapper">
    <div
      class="position-fixed bottom-0 right-0 p-3"
      style="z-index: 5; right: 0; bottom: 0"
    >
      <Notifier
        v-for="(notifier, index) in notifiers"
        :key="index"
        :result="notifier.result"
        @closeMe="destroyNotifier"
      >
        <template v-slot:header>
          {{ notifier.notifierName }}
        </template>
        <template v-slot:body>
          {{ notifier.notifierMessage }}
        </template>
      </Notifier>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import Notifier from "./Notifier.vue";
export default {
  name: "NotifierWrapper",
  components: {
    Notifier,
  },
  data() {
    return {
      notifiers: [],
    };
  },
  methods: {
    addNotifier(notifierName, notifierMessage, result) {
      this.notifiers.push({
        "notifierName": notifierName,
        "notifierMessage": notifierMessage,
        "result": result,
      });
      new Vue({});
    },
    destroyNotifier(key) {
      this.notifiers.splice(key, 0);
    },
  },
};
</script>

<style>
</style>