<template>
  <v-row justify="start" class="mx-5 my-0">
    <UndoButton />
    <RedoButton />

    <v-divider vertical class="mx-1 my-1" />

    <BoldButton />
    <ItalicButton />
    <StrikeThroughButton />

    <v-divider vertical class="mx-1 my-1" />
    <TextColorButton />
  </v-row>
</template>

<script>
import UndoButton from "./QuickActionButtons/UndoButton.vue";
import RedoButton from "./QuickActionButtons/RedoButton.vue";
import BoldButton from "./QuickActionButtons/BoldButton.vue";
import ItalicButton from "./QuickActionButtons/ItalicButton.vue";
import StrikeThroughButton from "./QuickActionButtons/StrikeThroughButton.vue";
import TextColorButton from "./QuickActionButtons/TextColorButton.vue";
export default {
  name: "QuickActionBar",
  components: {
    UndoButton,
    RedoButton,
    BoldButton,
    ItalicButton,
    StrikeThroughButton,
    TextColorButton,
  },
};
</script>

<style>
</style>