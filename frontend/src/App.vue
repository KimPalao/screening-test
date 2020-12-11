<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn text>
        <router-link to="/" class="white--text"> Home </router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/values" class="white--text"> Values </router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/principles" class="white--text">
          Principles
        </router-link>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>
