<template>
  <div>
    <ul id="sidebar-nav" class="nav flex-column">
      <NavLinkButton
        v-for="(navLink, index) in navLinks"
        :key="index"
        :sectionId="navLink.id"
        :linkTitle="navLink.title"
      />
    </ul>
  </div>
</template>

<script>
import NavLinkButton from "./NavLinkButton.vue";
export default {
  name: "SideNav",
  components: { NavLinkButton },
  data: () => {
    return {
      navLinks: null,
    };
  },
  mounted() {
    this.navLinks = navLinks;
    navLinks = null;
    $("#vue-side-navigation-js").remove();
  },
};
</script>

<style>
</style>