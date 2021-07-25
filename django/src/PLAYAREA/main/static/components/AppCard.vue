<template>
  <div class="card mb-3">
    <div class="card-header">{{ cardHeader }}</div>
    <div class="card-body">
      <h5 class="card-title">{{ cardTitle }}</h5>
      <p class="card-text">{{ cardText }}</p>
      <a
        v-if="subApps === null || !subApps.length"
        :href="'/apps/' + destination"
        class="btn btn-primary"
        >{{ cardButtonText }}</a
      >
      <div v-else>
        <button class="btn btn-primary" @click="showModal = true">
          {{ cardTitle }}
        </button>
        <Modal
          :open="showModal"
          :save="false"
          :additionalClasses="'modal-dialog-scrollable'"
          @done="closeModal()"
        >
          <template v-slot:modal-title>
            {{ cardTitle }}
          </template>
          <template v-slot:modal-body>
            <div class="container mt-3">
              <div class="row p-4">
                <div
                  class="col-12 mx-2 my-auto"
                  v-for="app in subApps"
                  :key="app.id"
                >
                  <!-- bei :destination ternary benutzen -->
                  <AppCard
                    class=""
                    :cardHeader="app.name"
                    :cardTitle="app.name"
                    :cardText="app.name"
                    :cardButtonText="app.name"
                    :destination="destination + app.href"
                  >
                  </AppCard>
                </div>
              </div>
            </div>
          </template>
        </Modal>
      </div>
    </div>
  </div>
</template>

<script>
import Modal from "@app/static/components/Modal.vue";
export default {
  name: "AppCard",
  components: {
    Modal,
  },
  data: function () {
    return {
      showModal: false,
    };
  },
  props: {
    cardHeader: {
      type: String,
      required: true,
    },
    cardTitle: {
      type: String,
      required: true,
    },
    cardText: {
      type: String,
      required: true,
    },
    cardButtonText: {
      type: String,
      required: true,
    },
    destination: {
      type: String,
      default: null,
    },
    subApps: {
      type: Array,
      default: null,
    },
  },
  methods: {
    openModal: function () {
      this.showModal = true;
    },
    closeModal: function () {
      this.showModal = false;
    },
  },
};
</script>

<style>
</style>