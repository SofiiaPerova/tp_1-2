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
            <router-link to="/profile" class="nav-link">Профиль</router-link>
            <a class="nav-link" @click="logout">Выход</a>
          </div>
        </div>
      </div>
    </nav>
    <div class="container">
      <h1 class="text-center mt-5">Внесение показаний</h1>
      <h3 class="text-center mt-5">{{ error }}</h3>
      <div class="row my-5 mx-auto" style="justify-content: center">
        <div class="col-md-5 card" style="border-radius: 15px">
          <div class="card-body">
            <form @submit.prevent>
              <input
                type="text"
                class="form-control"
                placeholder="Газ"
                v-model="gas"
              />
              <hr class="mx-n3" />

              <input
                type="text"
                class="form-control"
                placeholder="Водоснабжение"
                v-model="water"
              />
              <hr class="mx-n3" />
              <input
                type="text"
                class="form-control"
                placeholder="Электроэнергия"
                v-model="electro"
              />

              <hr class="mx-n3" />
            </form>
            <div></div>
            <div
              class="px-5 py-4"
              style="display: flex; justify-content: center"
            >
              <button
                type="submit"
                class="btn btn-primary btn-lg"
                @click="postIndicators"
              >
                Сформировать счет
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

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
  data: () => {
    return {
      gas: "",
      water: "",
      electro: "",
      gasError: "",
      waterError: "",
      electroError: "",
      error: "",
    };
  },
  methods: {
    logout() {
      localStorage.token = "";
      this.$router.push("/");
    },
    async postIndicators() {
      const refreshResponse = await axios.post(
        "http://127.0.0.1:8000/auth/jwt/refresh/",
        {
          refresh: localStorage.getItem("token"),
        }
      );
      const accessToken = refreshResponse.data.access;
      console.log(accessToken);

      axios
        .post(
          "http://127.0.0.1:8000/api/v1/user/inputMeter/",
          {
            gas: this.gas,
            water: this.water,
            electro: this.electro,
          },
          {
            headers: {
              Authorization: "Bearer " + accessToken,
            },
          }
        )
        .then((response) => {
          this.error = "Вы успешно внесли показания!";
          console.log(this.error);
        })
        .catch((error) => {
          this.error = error.response.data[0];
          console.log(error);
        });
    },
  },
  mounted() {},
};
</script>