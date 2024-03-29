import Vue from 'vue'
import VueRouter from 'vue-router'
import Register from '@/views/register'
import Main from '@/views/base-page'
import Authorization from '@/views/authorization'
import Indicators from '@/views/indications'
import PersonalAcc from '@/views/personal_account'
import Profile from '@/views/profile'
import RecoveryPass1 from '@/views/recovery_pass'
import RecoveryPass2 from '@/views/recovery_pass2'


Vue.use(VueRouter)

const routes = [
  { path: '/', component: Main },
  { path: '/register/', component: Register },
  { path: '/authorization', component: Authorization },
  { path: '/indicators', component: Indicators },
  { path: '/personal_account', component: PersonalAcc },
  { path: '/profile', component: Profile },
  { path: '/recovery_pass_1', component: RecoveryPass1 },
  { path: '/recovery_pass_2/:uidb64/:token/', component: RecoveryPass2 },

  
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router


{/* 

<router-link to="/authorization" class="nav-link">Вход</router-link>
<router-link to="/register" class="nav-link">Регистрация</router-link> 
<router-link to="/" class="nav-link">Главная</router-link>


*/}