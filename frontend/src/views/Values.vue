<template>
  <div class="home">
    <v-container>
      <v-row class="text-center">
        <v-col>
          <h2 class="text-h2">Values</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-form @submit.prevent="insert">
            <progress-overlay :value="submitting" />
            <fieldset :disabled="submitting" class="pa-4">
              <strong>Add New Value</strong>
              <v-container>
                <v-row>
                  <v-col cols="12" md="10">
                    <v-text-field
                      v-model="new_object.text"
                      label="Text"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    md="2"
                    class="d-flex flex-column justify-center"
                  >
                    <v-btn rounded color="primary" dark type="submit"
                      >Submit</v-btn
                    >
                  </v-col>
                </v-row>
              </v-container>
            </fieldset>
          </v-form>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="auto">&nbsp;</v-col>
        <v-col><strong>Text</strong></v-col>
        <v-col cols="auto"></v-col>
      </v-row>
      <!-- <v-row v-for="(value, index) in objects" :key="index">
        <v-col cols="auto">{{ index + 1 }}</v-col>
        <v-col>{{ value.text }}</v-col>
      </v-row> -->
      <editable-row
        pk="id"
        v-for="(object, index) in objects"
        v-model="objects[index]"
        :key="index"
        :index="index"
        :fields="fields"
        :update-url="update_url"
      >
      </editable-row>
    </v-container>
  </div>
</template>
<style scoped>
form {
  position: relative;
}
fieldset {
  border: 0;
}
</style>
<script>
import axios from "axios";
import ProgressOverlay from "@/components/ProgressOverlay.vue";
import EditableRow from "../components/EditableRow.vue";

export default {
  name: "Values",
  components: {
    ProgressOverlay,
    EditableRow,
  },
  data() {
    return {
      objects: [],
      new_object: {},
      submitting: false,
      loading: false,
      update_url: `${process.env.VUE_APP_BACKEND_URL}/api/values/`,
      fields: [
        {
          name: "text",
          type: "text",
        },
      ],
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
    async insert() {
      this.submitting = true;
      try {
        const response = await axios.put(
          `${process.env.VUE_APP_BACKEND_URL}/api/values`,
          this.new_object
        );
        if (response.status === 201) {
          this.get_data();
        }
      } catch (e) {
        console.log(e);
      } finally {
        this.submitting = false;
      }
    },
  },
  mounted() {
    this.get_data();
  },
};
</script>
