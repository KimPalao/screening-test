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

      <router-link to="/" class="white--text"> 
        <v-btn text>
          Home 
        </v-btn>
      </router-link>
      <router-link to="/values" class="white--text"> 
        <v-btn text>
          Values 
        </v-btn>
      </router-link>
      <router-link to="/principles" class="white--text">
        <v-btn text>
          Principles
        </v-btn>
      </router-link>
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
