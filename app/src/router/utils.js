import store from "../store";

export const handleMetaViews = (
  to,
  next
) => {
  if (to.matched.some((record) => record.meta.auth !== undefined)) {
    if (to.meta.auth) {
      if (!store.getters["auth/loggedIn"]) {
        next({ name: "home" });
        return true;
      }
    }
  }
  return false;
};
