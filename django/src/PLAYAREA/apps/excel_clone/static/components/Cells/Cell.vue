<template>
  <v-sheet
    color="white"
    elevation="1"
    :min-height="cellHeight"
    :min-width="cellWidth"
    @contextmenu="showMenu($event)"
  >
    <div
      ref="the-cell"
      class="overflow-hidden"
      :class="modeClassObj"
      :contenteditable="editable"
      :style="{
        maxHeight: cellHeight + 1 + 'px',
        maxWidth: cellWidth + 1 + 'px',
      }"
      :v-model="cellContent"
      @click="selectMode"
      @keydown.tab="selectCell($event)"
      @blur="updateCellValue"
    >
      {{ cellContent }}
    </div>
  </v-sheet>
</template>

<script>
import { mode } from "../../js/constants.js";
export default {
  name: "Cell",
  data: () => {
    return {
      cellHeight: 25,
      cellWidth: 100,

      showContextMenu: false,
      mode: { ...mode },
      cellContent: null,
    };
  },
  props: {
    cell: {
      Type: Object,
      required: true,
    },
  },
  computed: {
    modeClassObj: function () {
      let classValue = "border border-left-0";

      switch (this.cell?.mode) {
        case this.mode.EDIT:
          classValue = "edit-border";
          break;
        case this.mode.SELECT:
          classValue = "select-border";
          break;
        default:
          classValue = "border border-left-0";
          break;
      }
      return classValue;
    },
    editable: function () {
      return this.cell.mode === mode.EDIT || this.cell.mode === mode.SELECT
        ? true
        : false;
    },
  },
  watch: {
    cellContent: function (newValue) {
      this.cellContent = newValue;
    },
  },
  mounted() {
    this.cellContent = this.cell.content;
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
    selectMode() {
      if (this.cell?.mode === mode.SELECT) {
        this.$emit("modeSelected", mode.EDIT, this.cell);
        return;
      }

      this.$emit("modeSelected", mode.SELECT, this.cell);
    },
    selectCell(event) {
      this.cell.mode = mode.SELECT;
      this.$emit("tabPressed", event);
    },
    updateCellValue() {
      this.$emit(
        "cellContentUpdated",
        this.cell,
        this.$refs["the-cell"].innerHTML.replace(/^\n(\s){0,}/, "")
      );
    },
  },
};
</script>

<style scoped>
.edit-border {
  border: 1px solid blue;
  box-shadow: inset 1px 1px blue, inset -1px -1px blue;
  padding-left: 1px;
  padding-right: 1px;
}
.select-border {
  border: 1px solid green;
  box-shadow: inset 1px 1px green, inset -1px -1px green;
  padding-left: 1px;
  padding-right: 1px;
}
[contenteditable] {
  outline: none;
}
</style>