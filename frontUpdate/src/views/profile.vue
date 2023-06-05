<template>
  <div style="">
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
            <a href="#" class="nav-link" @click="logout">Выход</a>
          </div>
        </div>
      </div>
    </nav>
    <div class="container">
      <h1 class="text-center mt-5">Внесение показаний</h1>
      <h1 class="text-center mt-5" style="color: red;">{{ error }}</h1>
      <div class="row my-5 mx-auto" style="justify-content: center">
        <div class="col-lg-5 card" style="border-radius: 15px">
          <div class="card-body">
            <div class="mb-3 row">
              <label for="form1" class="col-sm-4 col-form-label">Фамилия</label>
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  id="form1"
                  :placeholder="last_name"
                  v-model="last_name"
                />
              </div>
            </div>

            <div class="mb-3 row">
              <label for="form2" class="col-sm-4 col-form-label">Имя</label>
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  id="form2"
                  :placeholder="first_name"
                  v-model="first_name"
                />
              </div>
            </div>

            <div class="mb-3 row">
              <label for="form3" class="col-sm-4 col-form-label"
                >Отчество</label
              >
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  id="form3"
                  :placeholder="second_name"
                  v-model="second_name"
                />
              </div>
            </div>

            <div class="mb-3 row">
              <label for="form4" class="col-sm-4 col-form-label"
                >Кол-во жильцов</label
              >
              <div class="col-sm-4">
                <input
                  type="text"
                  class="form-control"
                  id="form4"
                  :placeholder="residents"
                  v-model="residents"
                />
              </div>
            </div>

            <div
              class="px-5 py-4"
              style="display: flex; justify-content: center"
            >
              <button
                type="submit"
                class="btn btn-primary btn-lg"
                @click="update"
              >
                Сохранить
              </button>
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
      first_name: "",
      second_name: "",
      last_name: "",
      residents: "",
      error: "",
    };
  },

  methods: {
    logout() {
      localStorage.token = "";
      this.$router.push("/");
    },
    update() {
      axios
        .post(localStorage.ip + "auth/jwt/refresh/", {
          refresh: localStorage.getItem("token"),
        })
        .then((response) => {
          console.log(response);
          localStorage.accessToken = response.data.access;
          axios
            .patch(
              localStorage.ip + "api/v1/user/profile/",
              {
                first_name: this.first_name,
                second_name: this.second_name,
                last_name: this.last_name,
                residents: this.residents,
              },
              {
                headers: {
                  Authorization: `Bearer ${localStorage.accessToken}`,
                },
              }
            )
            .then((response) => {
              this.$router.push("/");
              console.log(response);
            })
            .catch((error) => {
              console.log(error);
              this.error = "Проверьте корректность введенных данных";
            });
        })
        .catch((error) => {
          console.log(error);
          this.error = "Проверьте корректность введенных данных";
        });
    },
  },
  mounted() {
    if (localStorage.getItem("token") == "") {
      this.$router.push("/");
    }
    axios
      .post( localStorage.ip +"auth/jwt/refresh/", {
        refresh: localStorage.getItem("token"),
      })
      .then((response) => {
        console.log(response);
        localStorage.accessToken = response.data.access;
        axios
          .get( localStorage.ip +"api/v1/user/profile/", {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          })
          .then((response) => {
            this.first_name = response.data.first_name;
            this.second_name = response.data.second_name;
            this.last_name = response.data.last_name;
            this.residents = response.data.residents;
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
<style>
.container4 {
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
