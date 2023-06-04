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
            <router-link to="/register" class="nav-link"
              >Регистрация</router-link
            >
          </div>
        </div>
      </div>
    </nav>
    <div class="container-fluid">
      <div class="row justify-content-center" style="text-align-last: center">
        <span class="heading">Восстановление пароля </span>
        <h2>{{ message }}</h2>
        <div class="col-md-5 col-12">
          <div class="form-outline mb-4" style="text-align-last: left">
            <input
              type="text"
              class="form-control"
              placeholder="Email"
              v-model="email"
            />
          </div>

          <div class="mb-4" style="justify-content: center; display: flex">
            <button
              class="btn btn-info btn-block"
              type="button"
              @click="sendEmail"
            >
              Восстановить пароль
            </button>
          </div>

         

          <p class="small mb-2">
            <a class="text-muted" href="#" @click="sendEmail"
              >Повторить отправку кода</a
            >
          </p>
        </div>
      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->
    <div class="container4">
      <footer class="footer mt-auto" style="padding-top: 3rem !important">
        <div
          class="text-center p-3"
          style="background-color: rgba(221, 238, 255, 1)"
        >
          <p class="text-dark" href="#">
            © 2023 Copyright: Телефон: 8-900-300-53-02. Почта:
            denistestfortp@mail.ru
          </p>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      error: "",
      message: "",
    };
  },

  methods: {
    async sendEmail() {
      const response = axios
        .post( localStorage.ip +"auth/password/reset/", {
          email: this.email,
        })
        .then((response) => {
          this.message =
            "Перейдите по ссылке в письме, чтобы задать новый пароль!";
        })
        .catch((error) => {
          console.log(error);
          this.message = "Неверные данные";
        });
    },
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
.container4 {
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>