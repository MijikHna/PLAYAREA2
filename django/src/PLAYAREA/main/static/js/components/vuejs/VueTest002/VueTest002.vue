<template>
  <Tabs class="m-2">
    <Tab title="Tab 1">Hello from Tab 1</Tab>
    <Tab title="Tab 2">Hello form Tab 2</Tab>
    <Tab title="Tab 3">Hello form Tab 3</Tab>
    <Tab title="Tab 4">Hello form Tab 4</Tab>
  </Tabs>
</template>

<script>
import Tabs from "./Tabs";
import Tab from "./Tab";

export default {
  components: {
    Tabs,
    Tab,
  },
  name: "VueTest002.vue",
};
</script>

<style></style>