<template>
  <li class="nav-item">
    <a href="#" class="nav-link" tabindex="-1" @click="showSection">{{
      linkTitle
    }}</a>
  </li>
</template>

<script>
export default {
  name: "NavLinkButton",
  data() {
    return {};
  },
  props: {
    linkTitle: String,
    sectionId: String,
  },
  methods: {
    showSection() {
      const allSectoinElems = $("div.section");

      if (this.sectionId === "general") {
        // show all Sections
        for (const section of allSectoinElems) {
          $(section).removeClass("d-none");
        }
      } else {
        // show only selected Section
        for (const section of allSectoinElems) {
          if (section.id === this.sectionId) {
            $(section).removeClass("d-none");
          } else {
            $(section).addClass("d-none");
          }
        }
      }

      if (window.matchMedia("(max-width: 600px)").matches) {
        toggleSideBar();
      }
    },
  },
};
</script>

<style>
</style>