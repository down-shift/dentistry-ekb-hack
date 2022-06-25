<script setup>
const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div class="card card-body">
    <div class="row">
      <div class="col">
        <img :src="props.data.image" alt="">
      </div>
      <div class="col"></div>
    </div>
  </div>
</template>
