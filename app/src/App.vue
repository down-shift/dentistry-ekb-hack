<script setup lang="ts">
import AtkNavbar from "./components/AtkNavbar.vue";
</script>

<template>
  <AtkNavbar />
  <router-view />
</template>

<style>
.card-shadow:hover {
  transition-property: box-shadow;
  transition-duration: 1s;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.15);
}

.rt-wp {
  padding-top: 60px;
}

h1 {
  font-size: 30px;
  font-weight: bold;
}

h2 {
  font-size: 25px;
  font-weight: bold;
}

h3 {
  font-size: 23px;
}

h4 {
  font-size: 20px;
}

body {
  margin-bottom: 320px;
  font-family: Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: 400;
}
</style>
