<template>
  <div ref="telegramRef" class="d-flex"></div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const emit = defineEmits(["callback"]);

const props = defineProps({
  mode: {
    type: String,
    required: true,
    validator(value) {
      return ["callback", "redirect"].includes(value);
    },
  },
  telegramLogin: {
    type: String,
    required: true,
    validator(value) {
      return value.endsWith("bot") || value.endsWith("Bot");
    },
  },
  redirectUrl: {
    type: String,
    default: "",
  },
  requestAccess: {
    type: String,
    default: "read",
    validator(value) {
      return ["read", "write"].includes(value);
    },
  },
  size: {
    type: String,
    default: "large",
    validator(value) {
      return ["small", "medium", "large"].includes(value);
    },
  },
  userpic: {
    type: Boolean,
    default: true,
  },
  radius: {
    type: String,
  },
});

const telegramRef = ref(null);

onMounted(() => {
  const script = document.createElement("script");
  window.onTelegramAuth = onTelegramAuth;
  script.async = true;
  script.src = "https://telegram.org/js/telegram-widget.js?3";
  script.setAttribute("data-size", props.size);
  script.setAttribute("data-userpic", props.userpic ? "true" : "false");
  script.setAttribute("data-telegram-login", props.telegramLogin);
  script.setAttribute("data-request-access", props.requestAccess);
  if (props.radius) script.setAttribute("data-radius", props.radius);

  if (props.mode === "callback") {
    script.setAttribute("data-onauth", "onTelegramAuth(user)");
  } else {
    script.setAttribute("data-auth-url", props.redirectUrl);
  }
  telegramRef.value?.appendChild(script);
});

const onTelegramAuth = (user) => {
  emit("callback", user);
};
</script>

