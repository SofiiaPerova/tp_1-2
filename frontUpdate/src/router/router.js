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
import Admin_1 from '@/views/admin_1'
import Admin_2 from '@/views/admin_2'
import Admin_CreateUser from '@/views/create_user'


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

  {path: '/admin', component: Admin_1},
  {path: '/admin_2/:id/', component: Admin_2},
  {path: '/admin/createUser', component: Admin_CreateUser},

  
]
//localStorage.ip = "http://45.146.164.34:8080/";
localStorage.ip = "http://127.0.0.1:8000/";
const router = new VueRouter({
  mode: 'history',
  routes
})

export default router



