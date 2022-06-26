<script setup>
import { marked } from "marked";

const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div class="card card-body mb-3" v-html="marked(data.text)"></div>
</template>
