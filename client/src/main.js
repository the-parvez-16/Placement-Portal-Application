import { createApp } from 'vue'
import App from '@/App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from '@/router';
import "@/assets/style.css";
import { VsxIcon } from "vue-iconsax";

const app = createApp(App);
app.use(router);
app.component("VsxIcon", VsxIcon);
app.mount('#app');
