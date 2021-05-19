<template>
  <div>
    <div
      ref="test-modal-001"
      class="modal fade"
      tabindex="-1"
      @click.self="cancel()"
      @keydown.esc="cancel()"
    >
      <div class="modal-dialog" :class="additionalClasses">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              <slot name="modal-title"></slot>
            </h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="cancel()"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <slot name="modal-body"></slot>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="cancel()">
              Close
            </button>
            <button type="button" class="btn btn-primary" @click="confirm()">
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    open: Boolean,
    additionalClasses: {
      type: String,
      default: "",
    },
  },
  watch: {
    open: function (newValue) {
      if (newValue === true) {
        $(this.$refs["test-modal-001"]).modal("show");
      } else {
        $(this.$refs["test-modal-001"]).modal("hide");
      }
    },
  },
  methods: {
    cancel() {
      this.$emit("done", null);
    },
    confirm() {
      const x = `Random Generator: ${Math.floor(Math.random() * 100)}`;
      this.$emit("done", x);
    },
  },
};
</script>

<style>
</style>