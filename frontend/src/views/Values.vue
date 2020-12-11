<template>
  <div class="home">
    <v-container>
      <v-row class="text-center">
        <v-col>
          <h2 class="text-h2">Values</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="auto">&nbsp;</v-col>
        <v-col><strong>Text</strong></v-col>
        <v-col cols="auto"></v-col>
      </v-row>
      <v-row v-for="(value, index) in objects" :key="index">
        <v-col cols="auto">{{ index + 1 }}</v-col>
        <v-col>{{ value.text }}</v-col>
        <v-col cols="auto">Delete</v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      objects: [],
    };
  },
  methods: {
    async get_data() {
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_BACKEND_URL}/api/values`,
          {
            params: {
              all: true,
            },
          }
        );
        this.objects = response.data.data;
      } catch (e) {
        console.log(e);
      }
    },
  },
  mounted() {
    this.get_data();
  },
};
</script>
