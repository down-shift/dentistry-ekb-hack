<script setup>
import { useStore } from "vuex";
import { onMounted, ref } from "vue";
import { getDentistAdvice } from "../api";
import AdviceCard from "./AdviceCard.vue";

const advice = ref([]);
const page = ref(1);

onMounted(() => {
  getDentistAdvice().then((data) => {
    advice.value = data.data;
  });
});
</script>

<template>
  <div class="container rt-wp">
    <div v-if="advice.length" v-for="req in advice">
      <AdviceCard :data="req" />
    </div>
    <div v-else class="text-center">Советы пока что не были добавлены</div>
  </div>
</template>
