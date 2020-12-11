<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row>
          <h3 class="text-h3">Values</h3>
        </v-row>
        <v-row>
          <v-col>
            <ol>
              <li v-for="(value, index) in values" :key="index" class="text-h5">
                {{ value.text }}
              </li>
            </ol>
          </v-col>
        </v-row>
      </v-col>
      <v-col>
        <v-row>
          <h3 class="text-h3">Principles</h3>
        </v-row>
        <v-row>
          <v-col>
            <ol>
              <li
                v-for="(principle, index) in principles"
                :key="index"
                class="text-h5"
              >
                {{ principle.text }}
              </li>
            </ol>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
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