<script setup>
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import TelegramLogin from "./TelegramLogin.vue";

const route = useRoute();
const store = useStore();
const router = useRouter();

const loggedIn = computed(() => store.getters["auth/loggedIn"]);

const processLogin = (data) => {
  store.dispatch("auth/loginuser", data);
};

const logout = () => {
  store.dispatch("auth/logout");
  router.push("/");
};
</script>

<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark py-3" id="mainNavbar">
    <div class="container">
      <router-link class="navbar-brand d-flex align-items-center py-0" to="/">
        <img
          src="@/assets/img/teeth.svg"
          alt=""
          width="30"
          class="d-inline-block me-3"
        />
        <span>зуб.чек</span>
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        id="mainNavbarToggler"
        data-bs-toggle="collapse"
        data-bs-target="#navbarContent"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
        <ul class="navbar-nav me-auto mb-lg-0 d-flex">
          <li class="nav-item">
            <router-link
              class="nav-link"
              aria-current="page"
              to="/"
              :class="{ active: route.name === 'home' }"
            >
              Анализ</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              aria-current="page"
              to="/advice"
              :class="{ active: route.name === 'advice' }"
            >
              Советы от стоматологов</router-link
            >
          </li>
        </ul>

        <form
          v-if="!loggedIn"
          class="d-flex align-items-center justify-content-center"
        >
          <TelegramLogin
            :mode="'callback'"
            :telegramLogin="'teethCheckBot'"
            :requestAccess="'write'"
            :userpic="false"
            radius="6"
            @callback="processLogin"
          />
        </form>
        <div v-else class="d-flex text-light align-items-center">
          <div class="dropdown">
            <div
              data-bs-toggle="dropdown"
              class="d-flex flex-row align-items-center"
            >
              <div class="me-3 fw-bold">
                {{ store.state.auth.user.username }}
              </div>
              <img :src="store.state.auth.user.photo_url" alt="" id="avatar" />
            </div>
            <ul class="dropdown-menu">
              <li>
                <router-link class="dropdown-item" to="/uploads"
                  ><i class="bi-clock-history me-2"></i>История</router-link
                >
              </li>

              <li>
                <a class="dropdown-item" href="#" @click.prevent="logout"
                  ><i class="bi-box-arrow-right me-2"></i>Выйти из аккаунта</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar-brand {
  font-size: 1.25rem;
  font-weight: bold;
  font-family: "VK Sans Display", sans-serif;
}

.social {
  font-size: 20px;
}

#avatar {
  border-radius: 50%;
  width: 40px;
}
</style>
