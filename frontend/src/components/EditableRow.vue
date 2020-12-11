<template>
  <v-row>
    <v-col cols="auto">{{ index + 1 }}</v-col>
    <v-col v-for="(field, index) in fields" :key="index">
      <div
        class="editable"
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
          @keyup.enter="focused = ''"
          @blur="focused = ''"
          :ref="field.name"
        ></v-text-field>
      </div>
    </v-col>
    <v-col cols="auto"
      ><v-btn icon color="red"><v-icon>mdi-delete</v-icon></v-btn></v-col
    >
  </v-row>
</template>

<script>
import axios from "axios";
export default {
  name: "EditableRow",
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
      focused: "",
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
      } catch (e) {
        console.log(e);
      } finally {
        this.submitting = false;
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
</style>