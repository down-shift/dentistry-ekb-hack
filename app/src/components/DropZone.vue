<template>
  <div>
    <div
      class="atk-box"
      @drag.prevent
      @dragstart.prevent
      @dragend.prevent="setBoxHighlight(false)"
      @dragover.prevent
      @dragenter.prevent="setBoxHighlight(true)"
      @dragleave.prevent="setBoxHighlight(false)"
      @drop.prevent="fileDropped"
      :class="{ 'atk-invalid': !isValid, 'is-dragover': boxHighlighted }"
    >
      <div class="text-center">
        <input
          id="file"
          type="file"
          ref="inputRef"
          class="box__file"
          @change.prevent="fileSelected"
          :multiple="multiple"
          :required="isRequired"
          :accept="accept"
          title=""
        />
        <label for="file" class="atk-dropzone-label">
          <strong>Выберите изображения</strong>
          <span> или перетащите их</span>
        </label>
        <div class="atk-error" v-if="boxError">
          {{ boxError }}
        </div>
        <div
          v-if="droppedFiles.length"
          class="mt-3 d-flex flex-column align-items-center filelist"
        >
          <table class="table table-sm">
            <tbody>
              <tr v-for="file in droppedFiles" :key="file">
                <td class="text-muted" style="width: 1%; white-space: nowrap">
                  {{ getFileSize(file.size) }}
                </td>
                <td>
                  {{ file.name }}
                </td>
                <td @click="deleteFile(file)">
                  <i class="bi-x-lg"></i>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const emit = defineEmits(["changed", "numchange"]);

const inputRef = ref(null);
const droppedFiles = ref([]);
const boxHighlighted = ref(false);
const boxError = ref("");

const isValid = computed(() => {
  return !boxError.value;
});

const setBoxHighlight = (s) => {
  boxHighlighted.value = s;
};

const submitForm = () => {
  boxError.value = "";
  let data = new FormData();
  if (droppedFiles.value.length) {
    droppedFiles.value.forEach((file) => data.append(props.name, file));
    emit("changed", data);
  }
};

const fileDropped = (e) => {
  setBoxHighlight(false);
  if (!props.multiple) droppedFiles.value = [];
  if (e.dataTransfer) {
    for (let file of e.dataTransfer.files) droppedFiles.value.push(file);
  }
  emit("numchange", droppedFiles.value.length);

  submitForm();
};

const fileSelected = () => {
  if (!props.multiple) droppedFiles.value = [];
  if (inputRef.value?.files?.length) {
    for (let file of inputRef.value.files) {
      if (!droppedFiles.value.includes(file)) droppedFiles.value.push(file);
    }
  }
  emit("numchange", droppedFiles.value.length);
  submitForm();
};

const clearInput = () => {
  droppedFiles.value = [];
  if (inputRef.value) inputRef.value.value = "";
};

const validate = () => {
  if (props.isRequired && droppedFiles.value.length === 0) {
    boxError.value = "Необходимо выбрать файл";
    return false;
  }
  return true;
};

const getFileSize = (size) => {
  let c = 0,
    s = size;
  const sizes = ["Б", "Кб", "Мб", "Гб"];
  while (s > 1024) {
    s /= 1024;
    c++;
  }
  return Math.round(s * 100) / 100 + " " + sizes[c];
};

const deleteFile = (file) => {
  const index = droppedFiles.value.findIndex((el) => el === file);
  if (index !== -1) droppedFiles.value.splice(index, 1);
  emit("numchange", droppedFiles.value.length);

  submitForm();
};

const props = defineProps({
  // Name that is used to pass dropped/selected files to `FormData`.
  name: { type: String, required: true },
  multiple: { type: Boolean, default: false },
  isRequired: { type: Boolean, default: true },
  accept: { type: String, default: "" },
});

defineExpose({ validate, droppedFiles, clearInput });
</script>

<style scoped>
:root {
  --bs-primary: #0d6efd;
  --bs-danger: #dc3545;
}

.atk-box.atk-invalid {
  outline: var(--bs-danger) dashed 2px;
}

.atk-box {
  font-size: 1rem;
  background-color: #f1f1f1;
  position: relative;
  outline: var(--bs-primary) dashed 2px;
  outline-offset: -10px;
  padding: 3rem;
  -webkit-transition: outline-offset 0.15s ease-in-out,
    background-color 0.15s linear;
  transition: outline-offset 0.15s ease-in-out, background-color 0.15s linear;
}

.atk-box.is-dragover {
  outline-offset: -20px;
  outline-color: #a1baff;
  background-color: #ffffff;
}

.box__file {
  width: 100%;
  height: 100%;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

.box__file + label {
  max-width: 80%;
  text-overflow: ellipsis;
  white-space: nowrap;
  cursor: pointer;
  display: inline-block;
  overflow: hidden;
}

.box__file + label:hover strong,
.box__file:focus + label strong,
.box__file.has-focus + label strong {
  color: var(--bs-primary);
}

.box__file:focus + label,
.box__file.has-focus + label {
  outline: 1px dotted #000000;
}

.atk-error {
  font-style: italic;
}

.atk-file-list {
  font-size: 0.8rem;
}

.filelist {
  white-space: nowrap;
  z-index: 9999;
}
</style>
