<template>
  <div class="mt-2">
    <ul class="nav">
      <li
        v-for="(tab, index) in tabs"
        :key="tab.title"
        @click="selectTab(index)"
        class="nav-item mx-2"
        :class="{ 'active text-primary': index == selectedIndex }"
      >
        {{ tab.title }}
      </li>
    </ul>
    <slot />
    <!-- slot wird weiter übergeben -->
  </div>
</template>

<script>
export default {
  name: "Tabs",
  data() {
    return {
      selectedIndex: 0,
      tabs: [],
    };
  },

  created() {
    this.tabs = this.$children;
  },
  mounted() {
    this.selectTab(0);
  },
  methods: {
    selectTab(i) {
      this.selectedIndex = i;

      this.tabs.forEach((tab, index) => {
        tab.isActive = index === i;
      });
    },
  },
};
</script>

<style>
</style>