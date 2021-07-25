<template>
  <div>
    <v-list-item link>
      <v-list-item-title @click="askTableName">{{ btnName }}</v-list-item-title>
    </v-list-item>

    <div ref="modal-title" v-show="showModalContent">
      <div class="text-h4">Table name</div>
    </div>
    <div ref="modal-body" v-show="showModalContent">
      <v-text-field
        v-model="tableName"
        :rules="rules"
        counter="25"
        hint="Enter the name of the new table"
        label="Table name"
      >
      </v-text-field>
    </div>
  </div>
</template>

<script>
import axios from "axios";

axios.defaults.xsrfCookieName = "XSRF-TOKEN";
export default {
  name: "NewButton",
  data: () => {
    return {
      btnName: "New",
      showModalContent: false,
      tableName: "",
      rules: [(v) => v.length <= 25 || "Max 25 characters"],
    };
  },
  methods: {
    askTableName() {
      globalThis.excelClone.$children[0].$refs["modal-simple"].$refs[
        "modal-simple-title"
      ].append(this.$refs["modal-title"]);
      globalThis.excelClone.$children[0].$refs["modal-simple"].$refs[
        "modal-simple-body"
      ].append(this.$refs["modal-body"]);
      globalThis.excelClone.$children[0].$refs[
        "modal-simple"
      ].confirmationFunction = this.createNewTable;
      globalThis.excelClone.$children[0].$refs["modal-simple"].declineFunction =
        this.clearInput;

      globalThis.excelClone.$children[0].$refs[
        "modal-simple"
      ].showDialog = true;

      this.showModalContent = true;
    },
    async createNewTable() {
      try {
        const response = await axios({
          method: "post",
          url: `/apps/excel-clone/new/`,
          data: {
            tableName: this.tableName,
          },
        });
      } catch (e) {
        // Error in der Message-Queue printen
        globalThis.notifier.$children[0].$refs.notifierWrapper.addNotifier(
          "Excel Clone",
          `Create New Table: ${e.message}`,
          e.name.toLowerCase()
        );
        this.tableName = "";
        return;
      }

      if (response.status === 200 || response.status === 201) {
        console.log("OK");
      } else {
        console.log("OK");
      }

      this.tableName = "";
    },
    clearInput() {
      this.tableName = "";
    },
  },
};
</script>

<style>
</style>