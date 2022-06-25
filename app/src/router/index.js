import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Uploads from "../components/Uploads.vue"
import Advice from "../components/Advice.vue"
import { handleMetaViews } from "./utils"

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/uploads",
    name: "uploads",
    component: Uploads,
    meta: {
      auth: true,
    }
  },
  {
    path: "/advice",
    name: "advice",
    component: Advice
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: [...routes],
  scrollBehavior() {
    return { top: 0 };
  },
});

router.beforeEach((to, from, next) => {
  document.body.setAttribute("tabindex", "-1");
  document.body.focus();
  document.body.removeAttribute("tabindex");

  const btn = document.getElementById("mainNavbarToggler");
  if (btn && !btn.classList.contains("collapsed")) {
    const content = document.getElementById("mainNavbarContent");
    if (content) {
      content.classList.remove("show");
      btn.classList.add("collapsed");
    }
  }

  const res = handleMetaViews(to, next);
  if (res) return;
  next();
});

export default router;
