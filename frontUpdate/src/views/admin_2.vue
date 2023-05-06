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
            <router-link to="/admin" class="nav-link"
              >Админка</router-link
            >
            <a class="nav-link" @click="logout">Выход</a>
          </div>
        </div>
      </div>
    </nav>
    <div class="container">
      <h3
        class="my-2 py-2"
        style="border: 1px solid rgb(240, 240, 240); text-indent: 10px"
      >
        Редактирование
      </h3>

      <div class="row ps-2">
        <div class="col-md-6 my-3">
          <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
            <label for="form1" class="col-sm-4 col-form-label">Email: </label>
            <div class="col-sm-8">
              <input
                v-bind:placeholder="resident.email"
                type="email"
                class="form-control"
                id="form1"
              />
            </div>
          </div>

          <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
            <label for="form2" class="col-sm-4 col-form-label"
              >Лицевой счет:
            </label>
            <div class="col-sm-8">
              <input
                v-bind:placeholder="resident.licSchet"
                type="text"
                class="form-control"
                id="form2"
              />
            </div>
          </div>

          <div class="mb-3 row pb-4" style="border-bottom: 1px solid #f0f0f0">
            <label for="form3" class="col-sm-4 col-form-label"
              >Кол-во жильцов:
            </label>
            <div class="col-sm-8">
              <input
                v-bind:placeholder="resident.residents"
                type="text"
                class="form-control"
                id="form3"
              />
            </div>
          </div>
        </div>
      </div>
      <div>
        <div>
          <div class="mb-4">
            <h4
              class="my-2 py-2"
              style="border: 1px solid rgb(240, 240, 240); text-indent: 10px"
            >
              Разрешения
            </h4>
          </div>

          <div class="form-check pb-2">
            <input
              v-if="resident.is_active == 'true'"
              class="form-check-input"
              type="checkbox"
              id="check1"
              checked
            />
            <input
              v-if="resident.is_active == 'false'"
              class="form-check-input"
              type="checkbox"
              id="check1"
              unchecked
            />
            <label class="form-check-label" for="check1">Активирован</label>
          </div>
          <div class="form-check pb-2">
            <input
              v-if="resident.is_staff == 'true'"
              class="form-check-input"
              type="checkbox"
              id="check2"
              checked
            />
            <input
              v-if="resident.is_staff == 'false'"
              class="form-check-input"
              type="checkbox"
              id="check2"
              unchecked
            />
            <label class="form-check-label" for="check2">Администратор</label>
          </div>
          <i-collapsible variant="light">
            <i-collapsible-item title="Показания счетчиков">
              <div v-for="data in resident.data" :key="data.id" class="table">
                <div class="row my-3 mx-auto" style="justify-content: center">
                  <div class="col-lg-9 card" style="border-radius: 15px">
                    <div class="card-body">
                      <div class="py-4" style="display: block">
                        <div class="mb-3 row">
                          <label class="col-sm-4 col-form-label" for="date1"
                            >Показания за:
                          </label>
                          <div class="col-sm-3">
                            <p id="date1">{{ data.date }}</p>
                          </div>
                          <button
                            type="submit"
                            class="col-sm-2 btn btn-primary"
                          >
                            Удалить
                          </button>
                        </div>
                      </div>
                      <div class="mb-3 row">
                        <label for="form1" class="col-sm-4 col-form-label"
                          >Показания газового счетчика:</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="text"
                            class="form-control"
                            id="form1"
                            :placeholder="data.gas"
                          />
                        </div>
                      </div>

                      <div class="mb-3 row">
                        <label for="form2" class="col-sm-4 col-form-label"
                          >Показания водяного счетчика:</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="text"
                            class="form-control"
                            id="form2"
                            :placeholder="data.water"
                          />
                        </div>
                      </div>

                      <div class="mb-3 row">
                        <label for="form3" class="col-sm-4 col-form-label"
                          >Показания счетчика энергии:</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="text"
                            class="form-control"
                            id="form3"
                            :placeholder="data.electro"
                          />
                         
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="pb-4"
                style="display: flex; justify-content: right"
              ></div>
            </i-collapsible-item>

            <i-collapsible-item title="Потребление услуг">
              <div v-for="cost in resident.costs" :key="cost.id" class="table">
                <div class="row my-3 mx-auto" style="justify-content: center">
                  <div class="col-lg-9 card" style="border-radius: 15px">
                    <div class="card-body">
                      <div class="py-4" style="display: block">
                        <div class="mb-3 row">
                          <label class="col-sm-4 col-form-label" for="date1"
                            >Потребление за:
                          </label>
                          <div class="col-sm-3">
                            <p id="date1">{{ cost.date }}</p>
                          </div>
                          <button
                            type="submit"
                            class="col-sm-2 btn btn-primary"
                          >
                            Удалить
                          </button>
                        </div>
                      </div>
                      <div class="mb-3 row">
                        <label for="form1" class="col-sm-4 col-form-label"
                          >потребления газа :</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="text"
                            class="form-control"
                            id="form1"
                            :placeholder="cost.gasCost"
                          />
                        </div>
                      </div>

                      <div class="mb-3 row">
                        <label for="form2" class="col-sm-4 col-form-label"
                          >Потребление воды :</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="text"
                            class="form-control"
                            id="form2"
                            :placeholder="cost.waterCost"
                          />
                        </div>
                      </div>

                      <div class="mb-3 row">
                        <label for="form3" class="col-sm-4 col-form-label"
                          >Потребление энергии :</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="text"
                            class="form-control"
                            id="form3"
                            :placeholder="cost.electroCost"
                          />
                          
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="pb-4"
                style="display: flex; justify-content: right"
              ></div>
            </i-collapsible-item>

            <i-collapsible-item title="Квитанции">
              <div
                v-for="invoice in resident.invoice"
                :key="invoice.id"
                class="table"
              >
                <div class="row my-3 mx-auto" style="justify-content: center">
                  <div class="col-lg-9 card" style="border-radius: 15px">
                    <div class="card-body">
                      <div class="py-4" style="display: block">
                        <div class="mb-3 row">
                          <label class="col-sm-4 col-form-label" for="date1"
                            >Квитанция за:
                          </label>
                          <div class="col-sm-3">
                            <p id="date1">{{ invoice.date }}</p>
                          </div>
                          <button
                            type="submit"
                            class="col-sm-2 btn btn-primary"
                          >
                            Удалить
                          </button>
                        </div>
                      </div>
                    </div>
                    <div class="mb-3 row">
                      <label for="form1" class="col-sm-4 col-form-label"
                        >Сумма за газ :</label
                      >
                      <div class="col-sm-8">
                        <input
                          type="text"
                          class="form-control"
                          id="form1"
                          :placeholder="invoice.gasSumm"
                        />
                      </div>
                    </div>

                    <div class="mb-3 row">
                      <label for="form2" class="col-sm-4 col-form-label"
                        >Сумма за воду :</label
                      >
                      <div class="col-sm-8">
                        <input
                          type="text"
                          class="form-control"
                          id="form2"
                          :placeholder="invoice.waterSumm"
                        />
                      </div>
                    </div>

                    <div class="mb-3 row">
                      <label for="form2" class="col-sm-4 col-form-label"
                        >Сумма за энергию :</label
                      >
                      <div class="col-sm-8">
                        <input
                          type="text"
                          class="form-control"
                          id="form2"
                          :placeholder="invoice.electroSumm"
                        />
                      </div>
                    </div>
                    <div class="mb-3 row">
                      <label for="form3" class="col-sm-4 col-form-label"
                        >Сумма за мусор :</label
                      >
                      <div class="col-sm-8">
                        <input
                          type="text"
                          class="form-control"
                          id="form4"
                          :placeholder="invoice.trashSumm"
                        />
                      </div>
                    </div>
                    <div class="mb-3 row">
                      <label for="form4" class="col-sm-4 col-form-label"
                        >Сумма за обслуживание дома :</label
                      >
                      <div class="col-sm-8">
                        <input
                          type="text"
                          class="form-control"
                          id="form5"
                          :placeholder="invoice.repairSumm"
                        />
                      </div>
                    </div>
                    <div class="mb-3 row">
                      <label for="form5" class="col-sm-4 col-form-label"
                        >Общая сумма :</label
                      >
                      <div class="col-sm-8">
                        <input
                          type="text"
                          class="form-control"
                          id="form6"
                          :placeholder="invoice.total"
                        />
    
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="pb-4"
                style="display: flex; justify-content: right"
              ></div>
            </i-collapsible-item>
          </i-collapsible>
        </div>
      </div>

      <hr />

      <div class="py-2" style="display: flex; justify-content: right">
        <button type="submit" class="btn btn-primary">Сохранить</button>
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
  data() {
    return {
      resident: [],
    };
  }, methods : {
    logout() {
      localStorage.token = "";
      this.$router.push("/");
    },
  },
  mounted() {
    // ${this.$route.params.uidb64}
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
          .get(
            `http://127.0.0.1:8000/api/v1/admin/user/${this.$route.params.id}/`,
            {
              headers: {
                Authorization: `Bearer ${localStorage.accessToken}`,
              },
            }
          )
          .then((response) => {
            this.resident = response.data;
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
</style>