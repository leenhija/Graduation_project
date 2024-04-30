import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import VueCookie from 'vue-cookie'
//import * as Argon from '@argonjs/argon'
import './axios'
const app = createApp(App)
app.use(createPinia())
app.use(router)
//app.use(VueCookies, { expires: '7d'})
app.mount('#app')
if (process.env.NODE_ENV !== 'production') {
    axios.defaults.baseURL = 'http://localhost:5000'; // Adjust if your server runs on a different port
  }