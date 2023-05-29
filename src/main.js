import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import axios, {isCancel, AxiosError} from 'axios';

console.log(axios.isCancel('something'));

createApp(App).use(router).mount('#app')

import "bootstrap/dist/js/bootstrap.js"
