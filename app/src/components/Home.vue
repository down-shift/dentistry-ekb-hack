<template>
  <div class="rt-wp container">
    <h1 class="title">зуб.чек</h1>
    <div class="text-muted mb-5">
      Искусственный интеллект для анализа состояния зубов по фотографии
    </div>

    <div v-if="!isLoading && outputData === null">
      <div>
        <div class="mb-3">
          <input
            class="form-control"
            type="file"
            id="formFile"
            @change="onFileChange"
          />
        </div>
      </div>

      <button
        v-if="postImage !== null"
        @click="processImage"
        class="btn btn-outline-primary"
      >
        Начать анализ
      </button>
    </div>
    <div v-else class="card">
      <span class="position-absolute" id="close-result" @click="clearOutput">
        <i class="bi bi-x-lg"></i>
      </span>
      <div class="card-body">
        <h2 class="title">Обработанное изображение</h2>

        <!-- <div class="bg-dark p-4">
          <code class="bg-dark">
            {{ outputData }}
          </code>
        </div> -->

        <div class="mt-4 d-flex justify-content-center align-items-center">
          <img :src="outputData.image" class="analysed_image w-50" />
        </div>

        <!-- 
        <div class="mt-5">
          <Result :data="outputData" />
        </div> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { analyseImage } from "../api";

const postImage = ref(null);
const isLoading = ref(false);
const outputData = ref(null);

const onFileChange = (e) => {
  const file = e.target.files[0];
  postImage.value = file;
};

const processImage = async () => {
  const fd = new FormData();
  fd.append("image", postImage.value);

  isLoading.value = true;
  analyseImage(fd).then((data) => {
    outputData.value = data.data;
    isLoading.value = false;
  });
};

const clearOutput = () => {
  postImage.value = null;
  outputData.value = null;
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
</style>
