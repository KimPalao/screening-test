<template>
  <v-overlay :absolute="true" :value="value">
    <v-progress-circular
      :size="size"
      :color="color"
      :indeterminate="indeterminate"
    ></v-progress-circular>
  </v-overlay>
</template>
<script>
export default {
  name: "ProgressOverlay",
  props: {
    value: {
      type: Boolean,
      required: true,
    },
    indeterminate: {
      type: Boolean,
      default: true,
    },
    size: {
      type: Number,
      default: 50,
    },
    color: {
      type: String,
      default: "primary",
    },
  },
};
</script>