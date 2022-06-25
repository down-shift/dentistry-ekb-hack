<template>
  <div class="rt-wp container">
    <h1 id="slogan">teeth.чек</h1>
    <div class="text-muted">Искусственный интеллект для анализа состояния зубов по фотографии</div>
  </div>
</template>

<style scoped>
.parallax {
  background: linear-gradient(43deg, #4158d0 0%, #d45fcd 46%, #ffbd43 100%);
  height: 120vh;
  color: white;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;
  -o-background-clip: text;
  -o-text-fill-color: transparent;
  background-size: 300%;
  animation: animated_text 10s ease-in-out infinite;
  -moz-animation: animated_text 10s ease-in-out infinite;
}
@keyframes animated_text {
  0% {
    background-position: 0px 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0px 50%;
  }
}
#hero {
  padding: 96px 32px;
  text-align: center;
}

#slogan {
  font-family: "VK Sans Display", sans-serif;
  font-weight: bold;
}
</style>
