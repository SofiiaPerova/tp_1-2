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
            <router-link to="/" class="nav-link">Главная</router-link>
          </div>
          <div class="navbar-nav">
            <router-link to="/register/" class="nav-link">Регистрация</router-link>
          </div>
        </div>
      </div>
    </nav>
    <div class="container-fluid">
      <div class="row justify-content-center" style="text-align-last: center">
        <span class="heading">Восстановление пароля</span>
        <p>{{ error }}</p>
        <div class="col-md-5 col-12">
          <div class="form-outline mb-4" style="text-align-last: left">
            <input
              type="password"
              class="form-control"
              placeholder="Новый пароль"
              v-model="password"
              @blur="validatePassword"
            />
          </div>

          <div class="form-outline mb-4" style="text-align-last: left">
            <input
              type="password"
              class="form-control"
              placeholder="Повторить пароль"
              v-model="re_password"
              @blur="validateRePassword"
            />
          </div>

          <div class="mb-4" style="justify-content: right; display: flex">
            <button class="btn btn-info btn-block" type="button" @click="reset_password">
              Восстановить пароль
            </button>
          </div>
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
      password: "",
      re_password: "",
      uidb64: "",
      token: "",
      error: "",
    }
  },
  methods : {
    async reset_password() {
      if(this.password != this.re_password) {
        this.error = "Пароли должны совпадать!"
        return
      } else {
        axios.post(`http://localhost:8000/auth/password/reset/confirm/${this.$route.params.uidb64}/${this.$route.params.token}/`, {
          password: this.password,
          re_password: this.re_password
        }).then((response) => {
          console.log(response);
          this.$router.push('/authorization');
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    validatePassword() {
      const passwordRegex =
        /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
      if (!passwordRegex.test(this.password)) {
        this.passwordError =
          "Пароль должен содержать не менее 8 символов, включая цифры, заглавные и строчные буквы";
      } else {
        this.passwordError = "";
      }
    },
    validateRePassword() {
      if (this.password != this.re_password) {
        this.re_passwordError = "Пароли не совпадают!";
      } else {
        this.re_passwordError = "";
      }
    },
  }
}
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