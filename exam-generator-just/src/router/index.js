import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/login.vue')
    },
    {
    path:'/signup',
    name:'signup',
    component:()=> import('../views/signup.vue')
    },
    
      {
      path:'/loggedin',
      name:'loggedin',
      component:()=>import('../views/loggedin.vue')
      },
      {
       path:'/profile',
       name:'profile',
       component:()=>import('../views/profile.vue')
      },
      {
        path:'/signin',
        name:'signin',
        component:()=> import('../views/signin.vue')
        } 
  ]
})
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.meta.requiresAuth && !token) {
    next('/login'); // Redirect to login if token is missing
  } else {
    next(); // Continue to the route
  }
});
export default router
