<script setup>
import { useStore } from "vuex";
import { onMounted, ref } from "vue";
import { getUploadsHistory } from "../api";
import HistoryCard from "./HistoryCard.vue";

const store = useStore();
const history = ref([]);
const page = ref(1);

onMounted(() => {
  if (store.getters["auth/loggedIn"])
    getUploadsHistory(store.state.auth.user.id).then((data) => {
      history.value = data.data;
    });
});
</script>

<template>
  <div class="container rt-wp">
    <div v-if="history && history.length" v-for="req in history">
      <HistoryCard :data="req"/>
    </div>
    <div v-else-if="history">
      <div class="text-center">
        Вы еще не загрузили ни одного файла
      </div>
    </div>
  </div>
</template>
