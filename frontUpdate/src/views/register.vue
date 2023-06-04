<template>
  <div>
    <nav
      class="navbar navbar-expand-lg navbar-light mb-5"
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
            <router-link to="/authorization" class="nav-link">Вход</router-link>
          </div>
        </div>
      </div>
    </nav>
    <div class="container-fluid">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12">
          <div
            class="card card-registration card-registration-2"
            style="border-radius: 15px"
          >
            <div class="card-body p-0">
              <div class="row g-0">
                <div class="col-lg-6">
                  <div class="p-5">
                    <h3 class="fw-normal mb-5" style="color: #4835d4">
                      Обязательные поля
                    </h3>
                    <div>
                      <h3>
                        <strong>{{ sucses }}</strong>
                      </h3>
                    </div>

                    <div class="form-outline mb-4">
                      <p v-if="licSchetError">{{ licSchetError }}</p>
                      <input
                        v-model="licSchet"
                        type="text"
                        id="form3Examplev2"
                        class="form-control form-control-lg"
                        @blur="validateLicSchet"
                      />

                      <label class="form-label" for="form3Examplev2"
                        >Лицевой счет</label
                      >
                    </div>

                    <div class="form-outline mb-4">
                      <p v-if="emailError">{{ emailError }}</p>
                      <input
                        v-model="email"
                        type="text"
                        id="form3Examplev3"
                        class="form-control form-control-lg"
                        @blur="validateEmail"
                      />

                      <label class="form-label" for="form3Examplev3"
                        >Email</label
                      >
                    </div>

                    <div class="form-outline mb-4">
                      <p v-if="passwordError">{{ passwordError }}</p>
                      <input
                        v-model="password"
                        type="password"
                        id="form3Examplev4"
                        class="form-control form-control-lg"
                        @blur="validatePassword"
                      />
                      <label class="form-label" for="form3Examplev4"
                        >Пароль</label
                      >
                    </div>

                    <div class="form-outline mb-4">
                      <p v-if="re_passwordError">{{ re_passwordError }}</p>
                      <input
                        v-model="re_password"
                        type="password"
                        id="form3Examplev5"
                        class="form-control form-control-lg"
                        @blur="validateRePassword"
                      />
                      <label class="form-label" for="form3Examplev5"
                        >Повторить пароль</label
                      >
                    </div>

                    <button
                      @click="registration"
                      type="button"
                      class="btn btn-light btn-lg mb-4"
                      style="float: right"
                      data-mdb-ripple-color="dark"
                    >
                      Register
                    </button>
                  </div>
                </div>
                <div class="col-lg-6 bg-indigo text-white">
                  <div class="p-5">
                    <h3 class="fw-normal mb-5">Необязательные поля</h3>

                    <div class="mb-4">
                      <div class="form-outline form-white">
                        <p v-if="lastNameError">{{ lastNameError }}</p>
                        <input
                          type="text"
                          id="form3Examplea3"
                          class="form-control form-control-lg"
                          @blur="validateLastName"
                        />
                        <label class="form-label" for="form3Examplea3"
                          >Фамилия</label
                        >
                      </div>
                    </div>
                    <div class="mb-4">
                      <div class="form-outline form-white">
                        <p v-if="firstNameError">{{ firstNameError }}</p>
                        <input
                          type="text"
                          id="form3Examplea6"
                          class="form-control form-control-lg"
                          @blur="validateFirstName"
                        />
                        <label class="form-label" for="form3Examplea6"
                          >Имя</label
                        >
                      </div>
                    </div>
                    <div class="mb-4">
                      <div class="form-outline form-white">
                        <input
                          type="text"
                          id="form3Examplea6"
                          class="form-control form-control-lg"
                        />
                        <label class="form-label" for="form3Examplea6"
                          >Отчество</label
                        >
                      </div>
                    </div>
                    <!--
                      <div class="row">
    
                        <div class="col-md-3 mb-4">
                          <div class="form-outline form-white">
                            <input type="text" id="form3Examplea4" class="form-control form-control-lg" />
                            <label class="form-label" for="form3Examplea4">Zip Code</label>
                          </div>
                        </div>
    
                        <div class="col-md-9 mb-4">
                          <div class="form-outline form-white">
                            <input type="text" id="form3Examplea5" class="form-control form-control-lg" />
                            <label class="form-label" for="form3Examplea5">Place</label>
                          </div>
                        </div>
    
                      </div>
                      -->

                    <div class="col-md-4 mb-4">
                      <div class="form-outline form-white">
                        <p v-if="residentsError">{{ residentsError }}</p>
                        <input
                          type="text"
                          id="form3Examplea6"
                          class="form-control form-control-lg"
                          @blur="validateResidents"
                        />
                        <label class="form-label" for="form3Examplea6"
                          >Кол-во жильцов</label
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
      licSchet: "",
      email: "",
      password: "",
      re_password: "",
      resdients: "",
      first_name: "",
      last_name: "",
      licSchetError: "",
      residentsError: "",
      firstNameError: "",
      lastNameError: "",
      emailError: "",
      passwordError: "",
      re_passwordError: "",
      sucses: "",
    };
  },

  methods: {
    async registration() {
      axios
        .post(localStorage.ip + "auth/users/", {
          licSchet: this.licSchet,
          email: this.email,
          password: this.password,
          re_password: this.re_password,
        })
        .then((response) => {
          this.sucses = "Для завершения регистрации подтвердите почту!";
          console.log(response);
        })

        .catch((error) => {
          error.response.data.email != null
            ? (this.emailError = error.response.data.email)
            : (this.emailError = "");
          error.response.data.licSchet != null
            ? (this.licSchetError = error.response.data.licSchet)
            : (this.licSchetError = "");
          this.error = error.response.data;
          console.log(error);
        });
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
    validateResidents() {
      const re = /\d/;
      if (!re.test(this.residents)) {
        this.residentsError = "Количество жильцов варьируется 1-9";
      } else {
        this.residentsError = "";
      }
    },
    validateFirstName() {
      const re = /[А-Я][а-я]{1,15}/;
      if (!re.test(this.firstName)) {
        this.firstNameError =
          "Имя состоит из букв русского алфавита и начинается с заглавной буквы";
      } else {
        this.firstNameError = "";
      }
    },
    validateLastName() {
      const re = /[А-Я][а-я]{1,15}/;
      if (!re.test(this.lastName)) {
        this.lastNameError =
          "Фамилия состоит из букв русского алфавита и начинается с заглавной буквы";
      } else {
        this.lastNameError = "";
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
  },
};
</script>
    
    
    
<style type="text/css">
@media (min-width: 1025px) {
  .h-custom {
    height: 100vh !important;
  }
}
.card-registration .select-input.form-control[readonly]:not([disabled]) {
  font-size: 1rem;
  line-height: 2.15;
  padding-left: 0.75em;
  padding-right: 0.75em;
}
.card-registration .select-arrow {
  top: 13px;
}

.gradient-custom-2 {
  /* fallback for old browsers */
  background: #a1c4fd;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(161, 196, 253, 1),
    rgba(194, 233, 251, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(161, 196, 253, 1),
    rgba(194, 233, 251, 1)
  );
}

.bg-indigo {
  background-color: #4835d4;
}
@media (min-width: 992px) {
  .card-registration-2 .bg-indigo {
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
  }
}
@media (max-width: 991px) {
  .card-registration-2 .bg-indigo {
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
  }
}
.container4 {
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
    