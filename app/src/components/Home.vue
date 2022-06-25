<template>
  <div class="rt-wp container" v-cloak>
    <h1 class="title">зуб.чек</h1>
    <div class="text-muted mb-5">
      Искусственный интеллект для проверки зубов на кариес по фотографии
    </div>

    <div v-if="!isLoading && outputData === null">
      <DropZone
        :multiple="true"
        ref="dropZone"
        name="images"
        :accept="'image/*'"
        @numchange="onFileUpload"
      />

      <div class="text-center mt-3">
        <button
          v-if="filesUploaded"
          @click="processImages"
          class="btn btn-outline-primary"
        >
          Начать анализ
        </button>
      </div>
    </div>
    <div v-else-if="isLoading && outputData !== null">
      <h2 class="title mb-4">Обработка изображений...</h2>
      <div class="progress" :key="progress">
        <div
          class="progress-bar"
          role="progressbar"
          :style="{
            width: progress + '%',
          }"
        ></div>
      </div>
    </div>
    <div v-else class="card">
      <span class="position-absolute" id="close-result" @click="clearOutput">
        <i class="bi bi-x-lg"></i>
      </span>
      <div class="card-body" id="output-data">
        <h2 class="title mb-4">Обработанные изображения</h2>

        <div v-for="obj in outputData">
          <div class="mt-3 row" v-if="obj.image !== null">
            <div
              class="col col-auto d-flex justify-content-center align-items-center"
            >
              <img :src="obj.image" class="analysed_image" />
            </div>
            <div class="col-auto">
              <div><b>Файл: </b>{{ obj.filename }}</div>
              <b>Обнаружено кариесов:</b> {{ obj.result.boxes.length }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { nextTick, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { analyseImage } from "../api";
import DropZone from "./DropZone.vue";

const isLoading = ref(false);
const outputData = ref(null);
const filesUploaded = ref(false);
const progress = ref(0);

const dropZone = ref(null);

const store = useStore();

const onFileUpload = (num) => {
  filesUploaded.value = Boolean(num);
};

const processImages = async () => {
  outputData.value = [];
  isLoading.value = true;
  const l = dropZone.value.droppedFiles.length;
  let c = 0;
  for (let file of dropZone.value.droppedFiles) {
    await processSingleImage(file);
    c++;
    progress.value = (c / l) * 100;
  }

  nextTick(() => {
    isLoading.value = false;

    nextTick(() => {
      const gallery = new Viewer(document.getElementById("output-data"));
    });
  });
};

const processSingleImage = async (file) => {
  const fd = new FormData();

  fd.append("image", file);

  if (store.getters["auth/loggedIn"])
    fd.append("tg_user", store.state.auth.user.id);

  const data = await analyseImage(fd);
  outputData.value.push(data.data);
};

const clearOutput = () => {
  outputData.value = null;
  filesUploaded.value = false;
};
</script>

<style scoped>
.title {
  font-family: "VK Sans Display", sans-serif;
  font-weight: bold;
}

#close-result {
  top: 10px;
  right: 10px;
  font-size: 1.3em;
  color: grey;
}

#close-result:hover {
  color: black;
}

.analysed_image {
  object-fit: scale-down;
  height: 100px;
  width: 100px;
}
</style>
