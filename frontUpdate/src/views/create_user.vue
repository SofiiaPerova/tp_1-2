<template>
  <div id="app1">
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
        <div
          class="row collapse navbar-collapse px-3 pt-2"
          id="navbarNavAltMarkup"
          style="align-items: flex-start"
        >
          <div class="col-4 navbar-nav mb-2 mb-lg-0">
            <router-link to="/personal_account" class="nav-link"
              >Главная</router-link
            >
          </div>
          <div class="col-4 navbar-nav" style="justify-content: center">
            <i
              class="bi bi-person-circle"
              style="font-size: 2rem"
              aria-hidden="true"
            ></i>
          </div>
          <div class="col-4 navbar-nav" style="justify-content: right">
            <router-link to="/admin" class="nav-link">Админка</router-link>
            <a href="#" class="nav-link" @click="logout">Выход</a>
          </div>
        </div>
      </div>
    </nav>
    <div class="container">
      <h1 class="text-center my-5">Создание пользователя</h1>
      <h3 v-if="error">{{ error }}</h3>
      <div class="row ps-2">
        <div class="container1">
          <div class="col-md-6 my-3">
            <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
              <p v-if="emailError">{{ emailError }}</p>
              <label for="form1" class="col-sm-4 col-form-label">Email: </label>
              <div class="col-sm-8">
                <input
                  v-model="email"
                  type="email"
                  class="form-control"
                  id="form1"
                  @blur="validateEmail"
                />
              </div>
            </div>

            <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
              <p v-if="licSchetError">{{ licSchetError }}</p>
              <label for="form2" class="col-sm-4 col-form-label"
                >Лицевой счет:
              </label>
              <div class="col-sm-8">
                <input
                  v-model="licSchet"
                  type="text"
                  class="form-control"
                  id="form2"
                  @blur="validateLicSchet"
                />
              </div>
            </div>
            <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
              <p v-if="passwordError">{{ passwordError }}</p>
              <label for="form2" class="col-sm-4 col-form-label"
                >Пароль:
              </label>
              <div class="col-sm-8">
                <input
                  v-model="password"
                  type="password"
                  class="form-control"
                  id="form2"
                  @blur="validatePassword"
                />
              </div>
            </div>
            <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
              <p v-if="re_passwordError">{{ re_passwordError }}</p>
              <label for="form2" class="col-sm-4 col-form-label"
                >Повторите пароль:
              </label>
              <div class="col-sm-8">
                <input
                  v-model="re_password"
                  type="password"
                  class="form-control"
                  id="form2"
                  @blur="validateRePassword"
                />
              </div>
            </div>
            <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
              <label for="form2" class="col-sm-4 col-form-label"
                >Администратор:
              </label>
              <div class="col-sm-8">
                <input
                  v-model="is_staff"
                  type="checkbox"
                  class="form-check-input"
                  id="form2"
                />
              </div>
            </div>
            <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
              <label for="form2" class="col-sm-4 col-form-label"
                >Активен:
              </label>
              <div class="col-sm-8">
                <input
                  v-model="is_active"
                  type="checkbox"
                  class="form-check-input"
                  id="form2"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="py-2" style="display: flex; justify-content: center">
        <button type="submit" class="btn btn-primary" @click="createUser()">
          Создать
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      licSchet: "",
      password: "",
      re_password: "",
      is_staff: "",
      is_active: "",
      licSchetError: "",
      emailError: "",
      passwordError: "",
      re_passwordError: "",
      error: "",
    };
  },
  methods: {
    logout() {
      localStorage.token = "";
      this.$router.push("/");
    },
    validateLicSchet() {
      const re = /\d{2}[A-Z]{2}\d{6}/;
      if (!re.test(this.licSchet)) {
        this.licSchetError =
          "Лицевой счет должен содержать 2 цифры + 2 заглавные латинские буквы + 6 цифр";
      } else {
        this.licSchetError = "";
      }
    },
    validateEmail() {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!re.test(this.email)) {
        this.emailError = "Некорректная почта";
      } else {
        this.emailError = "";
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
    async createUser() {
      if (localStorage.getItem("token") == "") {
        this.$router.push("/");
      }
      axios
        .post(localStorage.ip + "auth/jwt/refresh/", {
          refresh: localStorage.getItem("token"),
        })
        .then((response) => {
          localStorage.accessToken = response.data.access;
          axios
            .post(localStorage.ip + `api/v1/admin/createUser/`, {
              headers: {
                Authorization: `Bearer ${localStorage.accessToken}`,
              },
              email: this.email,
              licSchet: this.licSchet,
              password: this.password,
              is_staff: this.is_staff || false,
              is_active: this.is_active || false,
            })
            .then((response) => {
              this.$router.push("/admin");
              console.log(response);
            })
            .catch((error) => {
              error.response.data.email != null
                ? (this.emailError = error.response.data.email)
                : (this.emailError = "");
              error.response.data.licSchet != null
                ? (this.licSchetError = error.response.data.licSchet)
                : (this.licSchetError = "");
              console.log(error);
              console.log(error);
            });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {},
};
</script>

<style>
.container1 {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>