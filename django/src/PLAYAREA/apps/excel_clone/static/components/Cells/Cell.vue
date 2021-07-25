<template>
  <v-sheet
    color="white"
    elevation="1"
    :height="cellHeight"
    :width="cellWidth"
    @contextmenu="showMenu($event)"
  >
    <div class="border border-left-0">
      {{ cell.content }}
    </div>
  </v-sheet>
</template>

<script>
export default {
  name: "Cell",
  data: () => {
    return {
      cellHeight: 25,
      cellWidth: 100,

      showContextMenu: false,
      contextMenuX: 0,
      contextMenuY: 0,
    };
  },
  props: {
    cell: {
      Type: Object,
      required: true,
    },
  },
  methods: {
    showMenu(event) {
      event.preventDefault();

      const elPos = this.$el.getBoundingClientRect();
      const x = elPos.x + elPos.width / 2;
      const y = elPos.y - 56 + elPos.height / 2;

      const showCondition =
        globalThis.excelClone.$children[0].$refs["context-menu"].showContext;

      if (!showCondition) {
        globalThis.excelClone.$children[0].$refs[
          "context-menu"
        ].showContext = true;
        globalThis.excelClone.$children[0].$refs["context-menu"].x = x;
        globalThis.excelClone.$children[0].$refs["context-menu"].y = y;
        setTimeout(() => {
          globalThis.excelClone.$children[0].$refs["context-menu"].$el.focus();
        }, 0);
      }
    },
  },
};
</script>

<style>
</style>