<template>
  <li class="nav-item">
    <a href="#" class="nav-link" @click="showSection">{{ linkTitle }}</a>
  </li>
</template>

<script>
export default {
  name: "NavLinkButton",
  data() {
    return {
      linkTitle: null,
      sectionId: null,
    };
  },
  beforeMount() {
    this.linkTitle = this.$parent.$el.getAttribute("data-link-title");
    this.sectionId = this.$parent.$el.getAttribute("data-section-id");
  },
  methods: {
    showSection() {
      const allSectoinElems = $("div.section");
      if (this.sectionId === "general") {
        for (const section of allSectoinElems) {
          $(section).removeClass("d-none");
        }
        return;
      }

      for (const section of allSectoinElems) {
        if (section.id === this.sectionId) {
          $(section).removeClass("d-none");
        } else {
          $(section).addClass("d-none");
        }
      }
    },
  },
};
</script>

<style>
</style>