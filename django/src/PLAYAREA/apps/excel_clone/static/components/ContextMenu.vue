<template>
  <div
    v-show="showContext"
    class="context-menu-backdrop"
    @click.self="cancel"
    @keydown.esc="cancel"
    tabindex="-1"
  >
    <div>
      <v-list
        dense
        color="grey lighten-4"
        class="context-menu-popup"
        style="position: absolute"
        :style="{ top: y + 'px', left: x + 'px' }"
      >
        <v-list-item-group>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{ djangoTrans.entry1 }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title>{{ djangoTrans.entry2 }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContextMenu",
  data: () => {
    return {
      showContext: false,
      x: 0,
      y: 0,
      djangoTrans: {
        entry1: gettext("Entry 1"),
        entry2: gettext("Entry 2"),
      },
    };
  },
  props: {},
  methods: {
    cancel() {
      this.x = 0;
      this.y = 0;
      this.showContext = false;
    },
  },
};
</script>

<style scoped>
.context-menu-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  outline: none;
}
.context-menu-popup {
  min-width: 100px;
}
</style>