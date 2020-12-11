<template>
  <div class="home">
    <v-container>
      <v-row class="text-center">
        <v-col>
          <h1 class="text-h1">Agile Development</h1>
        </v-col>
      </v-row>
      <v-row>
        <home-list />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import HomeList from "../components/HomeList.vue";

export default {
  name: "Home",
  components: { HomeList },
};
</script>
