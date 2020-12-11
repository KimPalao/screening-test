<template>
  <div></div>
</template>

<script>
import axios from "axios";

export default {
  name: "MainList",
  data() {
    return {
      values: [],
      principles: [],
    };
  },
  methods: {
    async get_values() {
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_BACKEND_URL}/api/values`,
          {
            params: {
              all: true,
            },
          }
        );
        this.values = response.data.data;
      } catch (e) {
        console.log(e);
      }
    },
    async get_principles() {
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_BACKEND_URL}/api/principles`,
          {
            params: {
              all: true,
            },
          }
        );
        this.principles = response.data.data;
      } catch (e) {
        console.log(e);
      }
    },
  },
  mounted() {
    this.get_values();
    this.get_principles();
  },
};
</script>

<style>
</style>