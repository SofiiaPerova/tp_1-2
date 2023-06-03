<template>
  <div>
    <nav
      class="navbar navbar-expand-lg navbar-light"
      style="
        padding: 0.5rem 1rem;
        padding-top: 0.5rem;
        padding-right: 1rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        background-color: rgba(221, 238, 255, 1);
      "
    >
      <div class="container-fluid">
        <!-- <a class="navbar-brand" href="#">УК</a> -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup"
          aria-expanded="false"
          aria-label="Переключатель навигации"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav me-auto mb-2 mb-lg-0">
            <router-link to="/" class="nav-link active">Главная</router-link>
          </div>
          <div class="navbar-nav">
            <router-link to="/register" class="nav-link active"
              >Регистрация</router-link
            >
          </div>
        </div>
      </div>
    </nav>
    <div class="container-fluid">
      <div class="row justify-content-center" style="text-align-last: center">
        <div class="col-md-6 col-12">
          <span class="heading">АВТОРИЗАЦИЯ</span>
          <div>{{ loginError }}</div>
          <div class="form-outline mb-4" style="text-align-last: left">
            <input
              type="email"
              id="form2Example18"
              class="form-control form-control-lg"
              v-model="email"
            />
            <label class="form-label" for="form2Example18">Email</label>
          </div>

          <div class="form-outline mb-4" style="text-align-last: left">
            <input
              type="password"
              id="form2Example28"
              class="form-control form-control-lg"
              v-model="password"
            />
            <label class="form-label" for="form2Example28">Password</label>
          </div>
          
          <div class="mb-4" style="justify-content: right; display: flex">
            <button
              class="btn btn-info btn-lg btn-block px-5"
              type="button"
              @click="login"
              @submit.prevent
            >
              Login
            </button>
          </div>
          <p class="small mb-2">
            <router-link to="/recovery_pass_1" class="text-muted"
              >Forgot password?</router-link
            >
          </p>
          <p>
            Нет аккаунта?

            <router-link to="/register" class="link-info"
              >Регистрация</router-link
            >
          </p>
        </div>
      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->
    <footer class="footer mt-auto" style="padding-top: 3rem !important">
      <div
        class="text-center p-3"
        style="background-color: rgba(221, 238, 255, 1)"
      >
        <p class="text-dark" href="#">© 2023 Copyright: Контактные данные</p>
      </div>
    </footer>
  </div>
</template>



<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      password: "",
      token: "",
      loginError: "",
    };
  },

  methods: {
    async login() {
      try {
        const response = await axios
          .post(localStorage.ip + "auth/jwt/create/", {
            email: this.email,
            password: this.password,
          })
          .catch((error) => {
            console.log(error);
          });
        if (response) {
          localStorage.token = response.data.refresh;
          this.$router.push('/personal_account');
          this.token = localStorage.token;
        } else {
          this.loginError = "Неверный логин или пароль";
        }
        console.log(response.data);
        
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    if (localStorage.token) {
      this.token = localStorage.token;
      this.$router.push('/personal_account');
    } else {
      this.token = "";
    }
  },
};
</script>


<style>

/* Demo Background
body{background:url(/images/bg/bg-6.png)} */

/* Form Style */
.heading {
  display: block;
  font-size: 35px;
  font-weight: 700;
  padding: 35px 0;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 30px;
}
</style>