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
            <a class="nav-link active" href="#">Главная</a>
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
            <a class="nav-link" href="base_page.html">Выход</a>
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
              <b-table striped hover :items="residents" :fields="fields">
                <template #cell(email)="data">
                  <!-- `data.value` is the value after formatted by the Formatter -->
                  <a
                    :href="`/admin_2/${data.item.id}`"
                    >{{ data.value }}</a
                  >
                </template>
              </b-table>
            </tbody>
          </table>
        </div>
        <div class="col-lg-3">
          <ul class="list-group">
            <li class="list-group-item active" aria-current="true">Фильтр</li>
            <li class="list-group-item">
              <ul class="list-group my-2">
                <li class="list-group-item active" aria-current="true">
                  Статус персонала
                </li>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                >
                  Все
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                >
                  Администратор
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                >
                  Плательщик
                </button>
              </ul>
            </li>
            <li class="list-group-item">
              <ul class="list-group my-2">
                <li class="list-group-item active" aria-current="true">
                  Активация
                </li>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                >
                  Все
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                >
                  Активирован
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                >
                  Не активирован
                </button>
              </ul>
            </li>
          </ul>
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
  </div>
</template>

<script >
export default {
  data() {
    return {
      residents: [
        {
          id: 1,
          email: "admin@mail.ru",
          licSchet: "10XX111111",
          residents: "0",
          is_active: "true",
          is_staff: "true",
        },
        {
          id: 2,
          email: "resident2@mail.ru",
          licSchet: "20XX111111",
          residents: "3",
          is_active: "true",
          is_staff: "false",
        },
        {
          id: 3,
          email: "resident3@mail.ru",
          licSchet: "30XX111111",
          residents: "1",
          is_active: "true",
          is_staff: "false",
        },
      ],
      fields: [
        { key: "id", label: "id" },
        { key: "email", label: "Почта" },
        { key: "licSchet", label: "Почта" },
        { key: "is_active", label: "Active" },
        { key: "is_staff", label: "Статус" },
      ],
    };
  },
  methods: {
    email(value) {
      return `${value.first} ${value.last}`;
    },
  },
};
</script>

<style>
</style>