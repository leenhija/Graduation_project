import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { userStore } from "@/stores/user";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/login.vue"),
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/signup.vue"),
    },

    {
      path: "/loggedin",
      name: "loggedin",
      component: () => import("../views/loggedin.vue"),
    },
    {
      path: "/settings",
      name: "settings",
      component: () => import("../views/settings.vue"),
    },
    {
      path: "/materailandexamchar",
      name: "materailandexamchar",
      component: () => import("../views/materailandexamchar.vue"),
    },
    {
      path: "/editExam",
      name: "editExam",
      component: () => import("../views/editExam.vue"),
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import("../views/profile.vue"),
    },
    {
      path: "/privacyAndPolicy",
      name: "privacyAndPolicy",
      component: () => import("../views/privacyAndPolicy.vue"),
    },
    {
      path: "/team",
      name: "team",
      component: () => import("../views/team.vue"),
    },
  ],
});
router.beforeEach(async (to, from, next) => {
  const token = localStorage.getItem("token");
  if (token) {
    await userStore().getUser();
  }
  if (to.meta.requiresAuth && !token) {
    next("/login"); // Redirect to login if token is missing
  } else {
    return next(); // Continue to the route
  }
});
export default router;
