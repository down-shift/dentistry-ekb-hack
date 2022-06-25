<script setup>
import { useStore } from "vuex";
import { nextTick, onMounted, onUnmounted, ref } from "vue";
import { getUploadsHistory } from "../api";
import HistoryCard from "./HistoryCard.vue";

const store = useStore();
const history = ref([]);
const loading = ref(true);
const gallery = ref(null);

onMounted(() => {
  if (store.getters["auth/loggedIn"]) {
    loading.value = true;
    getUploadsHistory(store.state.auth.user.id).then((data) => {
      history.value = data.data;
      loading.value = false;

      nextTick(() => {
        gallery.value = new Viewer(document.getElementById("output-data"));
      });
    });
  }
});

onUnmounted(() => {
  gallery.value = null;
});
</script>

<template>
  <div class="container rt-wp" id="output-data">
    <div v-if="loading" class="text-center">
      <div class="spinner-border">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <div v-else>
      <div v-if="history && history.length" v-for="req in history">
        <div class="mt-3 row" v-if="req.image !== null">
          <div
            class="col col-auto d-flex justify-content-center align-items-center"
          >
            <img :src="req.image" class="analysed_image" />
          </div>
          <div class="col-auto">
            <div><b>Файл: </b>{{ req.filename }}</div>
            <b>Обнаружено кариесов:</b> {{ req.result.boxes.length }}
          </div>
        </div>
      </div>
      <div v-else-if="history">
        <div class="text-center">Вы еще не загрузили ни одного файла</div>
      </div>
    </div>
  </div>
</template>
