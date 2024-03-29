import Vue from 'vue'
import App from './App.vue'
import router from "./router/router";

import Inkline from '@inkline/inkline';
import '@inkline/inkline/dist/inkline.css';
import { BootstrapVue} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueApexCharts from 'vue-apexcharts'

Vue.use(Inkline);
Vue.use(BootstrapVue)
Vue.use(router)
Vue.use(VueApexCharts)

Vue.config.productionTip = false
Vue.component('apexchart', VueApexCharts)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
