<template>
  <canvas ref="canvas">
    <img :src="data.image" alt="" />
  </canvas>
</template>

<script setup>
import { nextTick, onMounted, ref } from "vue";

const canvas = ref(null);

const props = defineProps({
    data: {
        type: Object,
        required: true,
    }
})

onMounted(() => {
  nextTick(() => {
    const ctx = canvas.getContext("2d");


  });
});

</script>

<style></style>
