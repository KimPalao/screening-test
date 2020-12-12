<template>
  <v-row>
    <v-col cols="auto">{{ index + 1 }}</v-col>
    <v-col v-for="(field, index) in fields" :key="index">
      <div
        class="editable"
        :data-field="field.name"
        v-if="focused != field.name"
        @click="focused = field.name"
      >
        {{ value[field.name] }}
      </div>
      <div v-else>
        <v-text-field
          :value="value[field.name]"
          :type="field.type"
          @change="update(field.name, $event)"
          @blur="focused = ''"
          @input="errors[field.name] = ''"
          :ref="field.name"
          :error-messages="errors[field.name]"
        ></v-text-field>
      </div>
    </v-col>
    <v-col cols="auto">
      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon color="red" v-bind="attrs" v-on="on"
            ><v-icon>mdi-delete</v-icon></v-btn
          >
        </template>

        <v-card>
          <v-card-title class="headline grey lighten-2">
            Confirm Deletion
          </v-card-title>

          <v-card-text class="pa-4">
            Are you sure you want to delete {{ value[label] }}?</v-card-text
          >

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="remove(value[pk])"
              class="confirm-delete"
            >
              Confirm
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-col>
    <progress-overlay :value="submitting" />
  </v-row>
</template>

<script>
import axios from "axios";
import ProgressOverlay from "@/components/ProgressOverlay.vue";
export default {
  name: "EditableRow",
  components: {
    ProgressOverlay,
  },
  props: {
    value: {
      type: Object,
      readonly: true,
    },
    index: {
      type: Number,
      required: true,
    },
    pk: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    fields: {
      type: Array,
      required: true,
    },
    updateUrl: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      dialog: false,
      focused: "",
      submitting: false,
      errors: {},
    };
  },
  methods: {
    async update(key, value) {
      const data = { ...this.value };
      data[key] = value;
      this.submitting = true;
      try {
        await axios.patch(`${this.updateUrl}${this.value.id}`, data);
        this.$emit("input", { ...this.value, [key]: value });
        this.focused = "";
      } catch (e) {
        if (e.response) {
          this.errors = e.response.data.message;
        }
      } finally {
        this.submitting = false;
      }
    },
    async remove(key) {
      this.submitting = true;
      try {
        await axios.delete(`${this.updateUrl}${this.value.id}`);
        this.$emit("delete");
      } catch (e) {
      } finally {
        this.submitting = false;
        this.dialog = false;
      }
    },
  },
  watch: {
    focused(newVal) {
      if (newVal)
        this.$nextTick(() => {
          this.$refs[newVal][0].focus();
        });
    },
  },
};
</script>

<style scoped>
.editable {
  cursor: pointer;
}
.row {
  position: relative;
}
</style>