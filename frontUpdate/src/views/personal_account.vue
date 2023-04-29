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
    <div class="main">
      <div class="container">
        <h1 class="text-center mt-5" v-if="first_name">
          Добро пожаловать, {{ first_name + " " + second_name }}
        </h1>
        <h1 class="text-center mt-5" v-else>Добро пожаловать!</h1>
        <div class="row mt-5 mx-auto" style="justify-content: center">
          <h2
            class="text-center mt-5"
            v-if="dateError"
            style="padding-bottom: 2%"
          >
            {{ dateError }}
          </h2>
          <div class="col-md-4 mr-12" v-else>
            <div class="card">
              <b-icon-pencil-square
                style="
                  width: 117px;
                  height: 117px;
                  justify-content: center;
                  display: flex;
                  align-self: center;
                "
              ></b-icon-pencil-square>
              <div class="card-body" style="align-self: center">
                <router-link to="/indicators" class="btn btn-primary"
                  >Внесение показаний</router-link
                >
              </div>
            </div>
          </div>
          <div class="col-md-4 ml-12">
            <div class="card">
              <b-icon-clipboard-data
                style="
                  width: 117px;
                  height: 117px;
                  justify-content: center;
                  display: flex;
                  align-self: center;
                "
              ></b-icon-clipboard-data>

              <div class="card-body" style="align-self: center">
                <a href="#previous_data" class="btn btn-primary"
                  >Прошедший период</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container-2">
        <div class="invoice-2">
          <h2>Текущий чек</h2>
          <div class="invoice-items">
            <div class="invoice-item">
              <span class="item-label">Сумма за газ:</span>
              <span class="item-value">{{ invoice_last.gasSumm }} ₽</span>
            </div>
            <div class="invoice-item">
              <span class="item-label">Сумма за воду:</span>
              <span class="item-value">{{ invoice_last.waterSumm }} ₽</span>
            </div>
            <div class="invoice-item">
              <span class="item-label">Сумма за энергию:</span>
              <span class="item-value">{{ invoice_last.electroSumm }} ₽</span>
            </div>
            <div class="invoice-item">
              <span class="item-label">Обслуживание дома:</span>
              <span class="item-value"
                >{{
                  Number(invoice_last.trashSumm) +
                  Number(invoice_last.repairSumm)
                }}
                ₽</span
              >
            </div>
            <div class="invoice-item">
              <span class="item-label">Общая сумма:</span>
              <span class="item-value">{{ invoice_last.total }} ₽</span>
            </div>
          </div>
        </div>
      </div>
      <hr class="mx-5" id="previous_data" />
      <div class="container">
        <h1 class="text-center mt-5">Данные за прошедший период</h1>
        <div class="row mt-5 mx-auto" style="justify-content: center">
          <div class="col-md-4 my-auto mx-auto">
            <div class="list-group list-group-flush">
              <div class="buttons">
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                  @click="invoice(1)"
                >
                  Прошлый месяц
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                  @click="invoice(2)"
                >
                  Два месяца назад
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                  @click="invoice(3)"
                >
                  Три месяца назад
                </button>
              </div>
            </div>
          </div>
          <div class="col-md-4 mx-auto">
            <div class="p-5 mx-7">
              <div class="container-2">
                <div class="invoice-2">
                  <h2>Чек на оплату</h2>
                  <div class="invoice-items">
                    <div class="invoice-item">
                      <span class="item-label">Сумма за газ:</span>
                      <span class="item-value" v-if="invoiceActual.gasSumm"
                        >{{ invoiceActual.gasSumm }} ₽</span
                      >
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Сумма за воду:</span>
                      <span class="item-value" v-if="invoiceActual.waterSumm"
                        >{{ invoiceActual.waterSumm }} ₽</span
                      >
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Сумма за энергию:</span>
                      <span class="item-value" v-if="invoiceActual.electroSumm"
                        >{{ invoiceActual.electroSumm }} ₽</span
                      >
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Обслуживание дома:</span>
                      <span class="item-value" v-if="invoiceActual.trashSumm"
                        >{{
                          Number(invoiceActual.trashSumm) +
                          Number(invoiceActual.repairSumm)
                        }}
                        ₽</span
                      >
                      <!-- <span class="item-value">₽</span> -->
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Общая сумма:</span>
                      <span class="item-value" v-if="invoiceActual.total"
                        >{{ invoiceActual.total }} ₽</span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <br />
      <br />
      <hr class="mx-5" />
      <h1 class="text-center mt-5">Статистика потребления</h1>
      <div class="container py-5">
        <div class="row mt-5 mx-auto" style="justify-content: center">
          <div class="col-md-4 my-auto mx-auto">
            <div class="list-group list-group-flush">
              <div class="buttons">
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                  @click="getGas"
                >
                  Газ
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                  @click="getWater"
                >
                  Водоснабжение
                </button>
                <button
                  type="button"
                  class="list-group-item list-group-item-action"
                  @click="getElectro"
                >
                  Электроэнергия
                </button>
              </div>
            </div>
          </div>

          <div class="col-md-4 mx-auto">
            <div class="container" id="previous_data"></div>
            <!-- <h1 class="text-center mt-5">Статистика потребления</h1> -->
            <div class="container-3">
              <div class="p-5 mx-4">
                <div class="container-3">
                  <apexchart
                    class="chart"
                    ref="chart"
                    width="600"
                    height="350"
                    type="bar"
                    :options="options"
                    :series="series"
                    :xaxis="xaxis"
                  ></apexchart>
                </div>
              </div>
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
  data() {
    return {
      invoiceActual: {},
      invoice_last: {},
      Invoices: [{}],
      gas: [],
      water: [],
      electro: [],
      costsDate: [],
      costs: [],
      date: [],
      first_name: "",
      second_name: "",
      dateError: "",
      options: {
        chart: {
          height: 750,
          id: "vuechart-example",
          toolbar: {
            show: false, // отключаем панель инструментов
          },
        },
        tooltip: {
          enabled: true, // включить отображение подсказки
          followCursor: true, // следовать за курсором мыши
          marker: {
            show: false,
          },
          x: {
            show: true, // отображать значение оси x
          },
          y: {
            formatter: function (val) {
              return val.toFixed(0);
            },
          },
        },
      },
      xaxis: {
        type: "datetime",
        categories: [],
      },

      series: [
        {
          name: "Потраченно в этом месяце ",
          data: [],
        },
      ],
    };
  },

  methods: {
    logout() {
      localStorage.token = "";
      this.$router.push("/");
    },
    invoice(index) {
      const count = this.Invoices.length;
      this.invoiceActual = this.Invoices[count - index];
    },

    getGas(index) {
      const chart = this.$refs.chart.chart;
      chart.updateSeries([
        {
          data: this.gas,
        },
      ]);
      chart.updateOptions({
        xaxis: {
          categories: this.costsDate,
        },
      });
    },
    getWater() {
      const chart = this.$refs.chart.chart;
      chart.updateSeries([
        {
          data: this.water,
        },
      ]);
      chart.updateOptions({
        xaxis: {
          categories: this.costsDate,
        },
      });
    },
    getElectro() {
      const chart = this.$refs.chart.chart;
      chart.updateSeries([
        {
          data: this.electro,
        },
      ]);
      chart.updateOptions({
        xaxis: {
          categories: this.costsDate,
        },
      });
      console.log(this.date);
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
          .get("http://127.0.0.1:8000/api/v1/user/userData/", {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          })
          .then((response) => {
            this.Invoices = response.data.invoice;
            const count = this.Invoices.length;
            this.invoice_last = this.Invoices[count - 1];
            this.second_name = response.data.second_name;
            this.first_name = response.data.first_name;

            response.data.costs.forEach((cost) => {
              this.gas.push(cost.gasCost);
              this.costsDate.push(cost.date);
              this.water.push(cost.gasCost);
              this.electro.push(cost.gasCost);
            });
            const count2 = this.costsDate.length;
            const date = new Date(this.costsDate[count2 - 1]);

            const currentYear = new Date().getFullYear();
            const currentMonth = new Date().getMonth() + 1;
            const year = date.getFullYear();
            const month = date.getMonth() + 1;

            if (year === currentYear && month === currentMonth) {
              this.dateError = "Вы уже вводили показания в этом месяце!";
            }
            console.log(date);
            console.log(dateNow);
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
.main {
  border: 5px solid rgba(221, 238, 255, 1);
  padding: 10px;
  margin: 10px;
  margin-top: 0px;
  margin-bottom: 0px;
  border-radius: 10px;
  border-top: none;
}

.container-2 {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
  height: 70vh;
  width: 70vh !important;
}

.invoice-2 {
  border: 2px solid #333;
  padding: 50px;
  border-radius: 10px;
  width: 500px;
  text-align: center;
  font-size: 150%;
}

.invoice h2 {
  margin-top: 0;
  font-size: 2rem;
  text-transform: uppercase;
}

.invoice-items {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
}

.invoice-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.item-label {
  font-weight: bold;
}

.item-value {
  font-size: 1.2rem;
}
.buttons {
  border: 2px solid #333;
  padding: 20px;
  border-radius: 10px;
  font-size: 120%;
  height: 29vh;
  width: 60vh !important;
}
.list-group-item {
  display: inline-flex;
  height: 8vh;
  width: 55vh !important;
  margin-top: 10px;
  margin-right: 10px;
  margin-top: 0px;
}
</style>