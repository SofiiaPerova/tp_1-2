<template>
  <div>
    <nav class="row navbar navbar-expand-lg navbar-light"
    style="padding: .5rem 1rem;
    padding-top: 0.5rem;
    padding-right: 1rem;
    padding-bottom: 0.5rem;
    padding-left: 1rem;
    background-color: rgba(221, 238, 255, 1);">
    <div class="row mx-auto mb-2">
      <!-- <a class="navbar-brand" href="#">УК</a> -->
      <button class="col navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
      aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Переключатель навигации">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="navbar-collapse collapse" id="navbarNavAltMarkup" style="">
      <div class="col">
      <div class="navbar-nav" id="nav-first-child" style="align-items: center; text-align-last: center;">
        <router-link to="/personal_account" class="nav-link">Главная</router-link>
      </div>
      </div>
      <div class="col navbar-nav p-2" style="align-items: center;">
      <b-icon-person-circle
            style="width: 30px; height: 30px; justify-content: center; display: flex; align-self: center;">
            </b-icon-person-circle>
      </div>
      <div class="col">
      <div class="navbar-nav" style="align-items: center; text-align-last: center;">
        <router-link to="/profile" class="nav-link">Профиль</router-link>
      </div>
      <div class="navbar-nav" style="align-items: center; text-align-last: center;">
        <router-link to="/admin" class="nav-link" v-if="is_staff"
	    >Админка</router-link>
      </div>
      <div class="navbar-nav" style="align-items: center; text-align-last: center;">
            <a href="#" class="nav-link" @click="logout">Выход</a>
      </div>
      </div>
    </div>
  </div>
</nav>
    <div class="main m-5">
      <div class="container">
        <h1 class="text-center mt-5" v-if="first_name || last_name || second_name">
          Добро пожаловать, {{last_name + " " + first_name + " " + second_name}}
        </h1>
        <h1 class="text-center mt-5" v-else>Добро пожаловать!</h1>
        <div class="row m-5" style="justify-content: center">
          <h2
            class="text-center mt-5"
            v-if="dateError"
            style="padding-bottom: 2%"
          >
            {{ dateError }}
          </h2>
          <div class="col-md-4 pb-3" v-else>
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
          <div class="col-md-4 pb-3">
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

      <div class="col-8 col-md-5 col-xxl-3 mx-auto /*container-2*/">
        <div class="row py-4 invoice-2">
          <h2 style="text-align: center">Текущий чек</h2>
          <div class="row my-3 /*invoice-items*/">
            <div class="invoice-item">
              <span class="item-label">Сумма за газ:</span>
              <span class="item-value" v-if="invoice_last.gasSumm"
                >{{ invoice_last.gasSumm }} ₽</span
              >
            </div>
            <div class="invoice-item">
              <span class="item-label">Сумма за воду:</span>
              <span class="item-value" v-if="invoice_last.waterSumm"
                >{{ invoice_last.waterSumm }} ₽</span
              >
            </div>
            <div class="invoice-item">
              <span class="item-label">Сумма за энергию:</span>
              <span class="item-value" v-if="invoice_last.electroSumm"
                >{{ invoice_last.electroSumm }} ₽</span
              >
            </div>
            <div class="invoice-item">
              <span class="item-label">Обслуживание дома:</span>
              <span class="item-value" v-if="invoice_last.trashSumm"
                >{{
                  Number(invoice_last.trashSumm) +
                  Number(invoice_last.repairSumm)
                }}
                ₽
              </span>
            </div>
            <div class="invoice-item">
              <span class="item-label">Общая сумма:</span>
              <span class="item-value" v-if="invoice_last.total"
                >{{ invoice_last.total }} ₽</span
              >
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-center my-5">
        <b-button
          variant="primary"
          @click="deleteData"
          style="font-size: 20px"
          >Удалить последние внесенные показания</b-button
        >
      </div>

      <hr class="mx-5" id="previous_data" />
      <div class="container-5">
        <h1 class="text-center my-5 py-5">Данные за прошедший период</h1>
        <div class="row my-5 py-5 mx-auto" style="justify-content: center">
          <div class="col-md-5 my-auto mx-5">
          <div class="col-xs my-3">
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
          </div>
          <div class="col-8 col-md-4 mx-auto mt-5 /*container-2*/">

                <div class="row py-4 invoice-2">
                  <h2 style="text-align: center">Чек на оплату</h2>
                  <div class="row my-3 /*invoice-items*/">
                    <div class="invoice-item">
                      <span class="item-label">Сумма за газ:</span>
                      <span class="item-value" v-if="invoiceActual && invoiceActual.gasSumm"
                        >{{ invoiceActual.gasSumm }} ₽</span
                      >
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Сумма за воду:</span>
                      <span class="item-value" v-if="invoiceActual && invoiceActual.waterSumm"
                        >{{ invoiceActual.waterSumm }} ₽</span
                      >
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Сумма за энергию:</span>
                      <span class="item-value" v-if="invoiceActual && invoiceActual.electroSumm"
                        >{{ invoiceActual.electroSumm }} ₽</span
                      >
                    </div>
                    <div class="invoice-item">
                      <span class="item-label">Обслуживание дома:</span>
                      <span class="item-value" v-if="invoiceActual && invoiceActual.trashSumm"
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
                      <span class="item-value" v-if="invoiceActual && invoiceActual.total"
                        >{{ invoiceActual.total }} ₽</span
                      >
                    </div>
                  </div>

            </div>
          </div>
        </div>
      </div>
      <br />
      <br />
      <hr class="mx-5" />
      <h1 class="text-center my-5 pt-5">Статистика потребления</h1>
      <div class="container-4 py-5">
        <div class="row mt-5 mx-auto my-5 py-5" style="justify-content: center">
          <div class="col-md-5 my-auto me-2">
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

          <div class="col-md-6 mt-4" style="overflow: auto">

            <!-- <h1 class="text-center mt-5">Статистика потребления</h1> -->

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
      invoiceActual: {
        electroSumm: "",
        waterSumm: "",
        gasSumm: "",
        trashSumm: "",
        repairSumm: "",
      },
      invoice_last: {
        electroSumm: "",
        waterSumm: "",
        gasSumm: "",
        trashSumm: "",
        repairSumm: "",
      },
      Invoices: [{}],
      gas: [],
      water: [],
      electro: [],
      costsDate: [],
      costs: [],
      date: [],
      first_name: "",
      second_name: "",
      last_name: "",
      is_staff: "false",
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

    getGas() {
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
    async deleteData() {
      if (localStorage.getItem("token") == "") {
        this.$router.push("/");
      }
      axios
        .post(localStorage.ip + "auth/jwt/refresh/", {
          refresh: localStorage.getItem("token"),
        })
        .then((response) => {
          console.log(response);
          localStorage.accessToken = response.data.access;
          axios
            .delete(localStorage.ip + "api/v1/user/deleteLastData/", {
              headers: {
                Authorization: `Bearer ${localStorage.accessToken}`,
              },
            })
            .then((response) => {
              window.location.reload();
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
          .get( localStorage.ip +"api/v1/user/userData/", {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          })
          .then((response) => {
            this.second_name = response.data.second_name;
            this.first_name = response.data.first_name;
            this.last_name = response.data.last_name;
            this.is_staff = response.data.is_staff;
            if (response.data.invoice.length > 0) {
              this.Invoices = response.data.invoice;
              this.Invoices.sort((a, b) => new Date(a.date) - new Date(b.date));
              const count = this.Invoices.length;
              this.invoice_last = this.Invoices[count - 1];
            }  

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
            console.log(response.data);
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
@media (min-width: 992px) {
            div.col.navbar-nav {
                justify-content: center;
            }
            div.navbar-nav {
                float: right;
            }
            #nav-first-child {
                float: left;
            }
        }

.main {
  border: 5px solid rgba(221, 238, 255, 1);
  padding: 10px;
  margin: 10px;


  border-radius: 10px;

}

.container-1 {
  text-align: center;
  height: 20vh;
  width: 70vh !important;
}
*/

.container-2 {
  display: flex;
  justify-content: center;
  align-items: center;
  /*
  margin-left: auto;
  margin-right: auto;
  height: 70vh;
  width: 70vh !important;
  */
}
/* .container-4 {
  margin: 5%;
}

.container-5 {
  margin: 8%;
} */

.invoice-2 {
  border: 2px solid #333;
  justify-content: center;
  border-radius: 10px;
  /*
  padding: 50px;
  width: 500px;
  font-size: 150%;
  text-align: center;
  */

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
  /*
  height: 29vh;
  width: 60vh !important;
  */
}
.list-group-item {
  display: inline-flex;
  /*
  height: 8vh;
  width: 55vh !important;
  */
  margin-top: 10px;
  margin-right: 10px;
  margin-top: 0px;
}
</style>
