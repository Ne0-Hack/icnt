import {createRouter, createWebHistory} from "vue-router";

const routes = [
  {path: "/", name: "main", component: () => import("@templates/main/MainTemplate.vue")},
  {path: "/profile", name: "profile", component: () => import("@templates/profile/ProfileTemplate.vue")},
  {path: "/works", name: "works", component: () => import("@templates/WorkTemplate.vue")},
  {path: "/service/:serviceSlug", name: "service", component: () => import("@templates/ServiceTemplate.vue")},
  {path: "/news/:newsSlug", name: "news", component: () => import("@templates/NewsTemplate.vue")},
  {path: "/order/create", name: "order_create", component: () => import("@templates/OrderCreateTemplate.vue")},
  {path: "/order/review", name: "order_review", component: () => import("@templates/OrderReviewTemplate.vue")},
  {path: "/auth", children: [
      {path: "signin", name: "signin", component: () => import("@templates/auth/SignInTemplate.vue")},
      {path: "signup", name: "signup", component: () => import("@templates/auth/SignUpTemplate.vue")},
    ]
  },
]

export const router = createRouter({
  scrollBehavior() {
    return { top: 0 };
  },
  history: createWebHistory(),
  routes
})
