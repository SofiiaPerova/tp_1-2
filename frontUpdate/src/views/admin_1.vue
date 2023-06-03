<template style="height: 100vh; padding: 0 10%">
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
            <b-icon-person
              style="width: 30px; height: 30px"
              aria-hidden="true"
              class="rounded-circle"
              variant="black"
            ></b-icon-person>
          </div>
          <div class="col-4 navbar-nav" style="justify-content: right">
            <a class="nav-link" @click="logout">Выход</a>
          </div>
        </div>
      </div>
    </nav>
    <div class="container">
      <h1 class="text-center my-5">Аккаунт администрирования</h1>
      <h4 class="my-3">Выберите пользователя для изменений</h4>
      <div class="input-group">
        <div class="form-outline me-2">
          <input
            type="search"
            id="form1"
            class="form-control"
            placeholder="Search"
            v-model="searchValue"
          />
        </div>
        <button type="button" class="btn btn-primary">
          <b-icon-search></b-icon-search>
        </button>
      </div>

      <div class="row" style="margin-top: 20px">
        <div class="col-lg-9">
          <table class="table table-striped">
            <tbody>
              <b-table striped hover :items="filteredRole" :fields="fields">
                <template #cell(email)="data">
                  <!-- `data.value` is the value after formatted by the Formatter -->
                  <a :href="`/admin_2/${data.item.id}`">{{ data.value }}</a>
                </template>
              </b-table>
            </tbody>
          </table>
        </div>

        <div class="col-lg-3">
          <b-card
            header="Фильтры"
            header-bg-variant="primary"
            text-variant="white"
          >
            <b-card header="Статус персонала" header-bg-variant="primary">
              <b-list-group>
                <b-list-group-item
                  href="#"
                  @click="filterStatus = 'all'"
                  :active="filterStatus === 'all'"
                  button
                  class="w-75 h-75"
                >
                  Все
                </b-list-group-item>
                <b-list-group-item
                  href="#"
                  @click="filterStatus = 'admin'"
                  :active="filterStatus === 'admin'"
                  button
                  class="w-75 h-75"
                >
                  Администратор
                </b-list-group-item>
                <b-list-group-item
                  href="#"
                  @click="filterStatus = 'user'"
                  :active="filterStatus === 'user'"
                  button
                  class="w-75 h-75"
                >
                  Плательщик
                </b-list-group-item>
              </b-list-group>
            </b-card>

            <b-card header="Активация" header-bg-variant="primary">
              <b-list-group>
                <b-list-group-item
                  href="#"
                  @click="filterStatus = 'all'"
                  :active="filterStatus === 'all'"
                  button
                  class="w-75 h-75"
                >
                  Все
                </b-list-group-item>
                <b-list-group-item
                  href="#"
                  @click="filterStatus = 'active'"
                  :active="filterStatus === 'active'"
                  button
                  class="w-75 h-75"
                >
                  Активирован
                </b-list-group-item>
                <b-list-group-item
                  href="#"
                  @click="filterStatus = 'nactive'"
                  :active="filterStatus === 'nactive'"
                  button
                  class="w-75 h-75"
                >
                  Не активирован
                </b-list-group-item>
              </b-list-group>
            </b-card>
          </b-card>
        </div>
      </div>
    </div>

    <footer class="footer mt-auto" style="padding-top: 20rem !important">
      <div
        class="text-center p-3"
        style="background-color: rgba(221, 238, 255, 1)"
      >
        <p class="text-dark" href="#">© 2023 Copyright: Контактные данные</p>
      </div>
    </footer>
  </div>
</template>

<script >
import axios from "axios";
export default {
  data() {
    return {
      residents: [],
      searchValue: "",
      filterStatus: "all", // "all", "activ", "nactiv"
      fields: [
        { key: "id", label: "id" },
        { key: "email", label: "Почта" },
        { key: "licSchet", label: "Лицевой счет" },
        { key: "is_active", label: "Active" },
        { key: "is_staff", label: "Статус" },
      ],
    };
  },
  methods: {
    email(value) {
      return `${value.first} ${value.last}`;
    },
    logout() {
      localStorage.token = "";
      this.$router.push("/");
    },
  },
  computed: {
    filteredRole() {
    const search = this.searchValue.toLowerCase(); // Приведите значение поиска к нижнему регистру
    switch (this.filterStatus) {
      case "admin":
        return this.residents.filter((resident) => {
          // Примените фильтр исходя из значения поиска
          return resident.is_staff === true && resident.email.toLowerCase().includes(search);
        });
      case "user":
        return this.residents.filter((resident) => {
          // Примените фильтр исходя из значения поиска
          return resident.is_staff === false && resident.email.toLowerCase().includes(search);
        });
      case "active":
        return this.residents.filter((resident) => {
          // Примените фильтр исходя из значения поиска
          return resident.is_active === true && resident.email.toLowerCase().includes(search);
        });
      case "nactive":
        return this.residents.filter((resident) => {
          // Примените фильтр исходя из значения поиска
          return resident.licSchet.toLowerCase().includes(search);
        });
      default:
        return this.residents.filter((resident) => {
          // Примените фильтр исходя из значения поиска
          return resident.email.toLowerCase().includes(search) || resident.licSchet.toLowerCase().includes(search);
        });
    }
  },
  },
  mounted() {
    if (localStorage.getItem("token") == "") {
      this.$router.push("/");
    }
    axios
      .post("http://127.0.0.1:8000/auth/jwt/refresh/", {
        refresh: localStorage.getItem("token"),
      })
      .then((response) => {
        console.log(response);
        localStorage.accessToken = response.data.access;
        axios
          .get("http://127.0.0.1:8000/api/v1/admin/users/", {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          })
          .then((response) => {
            this.residents = response.data;
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
.footer {
  margin-top: 1000px;
  padding-top: auto;
}
</style>