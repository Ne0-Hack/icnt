import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import {router} from "./plugins/router/index.js";
import {store} from "@/plugins/store/index.js";
import axios from "axios";

// axios.defaults.baseURL = import.meta.env.VITE_API_ENDPOINT ?? null
axios.defaults.headers.common['Authorization'] = store.state.userToken


createApp(App).use(router).use(store).mount('#app')
