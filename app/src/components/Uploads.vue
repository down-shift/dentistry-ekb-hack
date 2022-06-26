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
      <div v-if="history && history.length" v-for="(obj, i) in history">
        <div class="mt-3 row" v-if="obj.image !== null">
          <div
            class="col col-auto d-flex justify-content-center align-items-center"
          >
            <img :src="obj.image" class="analysed_image mb-3" />
          </div>
          <div class="col-auto">
            <div><b>Файл: </b>{{ obj.filename }}</div>
            <b>Обнаружено кариесов:</b> {{ obj.result.boxes.length }}

            <div
              v-if="obj.result.boxes.length === 0"
              class="alert alert-success mt-3"
            >
              <i class="bi-check-lg me-2"></i>
              Кариесы не обнаружены. Обращайтесь к стоматологу раз в полгода.
            </div>
            <div
              v-else-if="obj.result.boxes.length <= 3"
              class="alert alert-warning mt-3"
            >
              <i class="bi-exclamation-lg me-2"></i>
              Зубы нуждаются в дополнительном уходе. Посещайте стоматолога раз в
              месяц.
            </div>
            <div v-else class="alert alert-danger mt-3">
              <i class="bi-x-lg me-2"></i>
              Зубы в плохом состоянии. Необходимо срочное посещение стоматолога.
            </div>
          </div>
        </div>
        <hr v-if="i !== history.length - 1" />
      </div>
      <div v-else-if="history">
        <div class="text-center">Вы еще не загрузили ни одного файла</div>
      </div>
    </div>
  </div>
</template>

<style>
.analysed_image {
  object-fit: scale-down;
  height: 100px;
  width: 100px;
}
</style>
