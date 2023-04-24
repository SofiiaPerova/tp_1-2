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
      <h1 class="text-center mt-5">Welcome to your personal account</h1>
      <div class="row mt-5 mx-auto" style="justify-content: center">
        <div class="col-md-4 mr-12">
          <div class="card">
            <i
              class="bi bi-pencil-square mt-3"
              style="
                font-size: 7rem;
                justify-content: center;
                display: flex;
                align-self: center;
              "
            ></i>
            <div class="card-body" style="align-self: center">
              <router-link to="/indicators" class="btn btn-primary"
                >Внесение показаний</router-link
              >
            </div>
          </div>
        </div>
        <div class="col-md-4 ml-12">
          <div class="card">
            <i
              class="bi bi-clipboard-data mt-3"
              style="
                font-size: 7rem;
                justify-content: center;
                display: flex;
                align-self: center;
              "
            ></i>
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
            <span class="item-value">{{ gas_actual }} ₽</span>
          </div>
          <div class="invoice-item">
            <span class="item-label">Сумма за воду:</span>
            <span class="item-value">{{ water_actual }} ₽</span>
          </div>
          <div class="invoice-item">
            <span class="item-label">Сумма за энергию:</span>
            <span class="item-value">{{ electro_actual }} ₽</span>
          </div>
          <div class="invoice-item">
            <span class="item-label">Сумма за обслуживание дома:</span>
            <span class="item-value">{{ za_dom_actual }} ₽</span>
          </div>
          <div class="invoice-item">
            <span class="item-label">Общая сумма:</span>
            <span class="item-value">{{ total_actual }} ₽</span>
          </div>
        </div>
      </div>
    </div>
    <div class="container" id="previous_data">
      <h1 class="text-center mt-5">Данные за прошедший период</h1>
      <div class="row mt-5 mx-auto" style="justify-content: center">
        <div class="col-md-4 my-auto mx-auto">
          <div class="list-group list-group-flush">
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
        <div class="col-md-4 mx-auto">
          <div class="p-5 mx-7">
            <div class="container-2">
              <div class="invoice-2">
                <h2>Чек на оплату</h2>
                <div class="invoice-items">
                  <div class="invoice-item">
                    <span class="item-label">Сумма за газ:</span>
                    <span class="item-value">{{ gas }} ₽</span>
                  </div>
                  <div class="invoice-item">
                    <span class="item-label">Сумма за воду:</span>
                    <span class="item-value">{{ water }} ₽</span>
                  </div>
                  <div class="invoice-item">
                    <span class="item-label">Сумма за энергию:</span>
                    <span class="item-value">{{ electro }} ₽</span>
                  </div>
                  <div class="invoice-item">
                    <span class="item-label">Обслуживание дома:</span>
                    <span class="item-value">{{ za_dom }} ₽</span>
                  </div>
                  <div class="invoice-item">
                    <span class="item-label">Общая сумма:</span>
                    <span class="item-value">{{ total }} ₽</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr class="mx-5" />
    <div class="container py-5">
      <div class="row mt-5 mx-auto" style="justify-content: center">
        <div class="col-md-4 my-auto mx-auto">
          <div class="list-group list-group-flush">
            <button
              type="button"
              class="list-group-item list-group-item-action"
              @click="get('getGasMeter')"
            >
              Газ
            </button>
            <button
              type="button"
              class="list-group-item list-group-item-action"
              @click="get('getWaterMeter')"
            >
              Водоснабжение
            </button>
            <button
              type="button"
              class="list-group-item list-group-item-action"
              @click="get('getElectroMeter')"
            >
              Электроэнергия
            </button>
          </div>
        </div>
        <div class="col-md-4 mx-auto">
          <h4 class="text-center">Статистика потребления</h4>
          <div class="p-5 mx-4">
            <i
              class="bi bi-card-image"
              style="
                font-size: 7rem;
                justify-content: center;
                display: flex;
                align-self: center;
              "
            >
              <apexchart
                ref="chart"
                width="500"
                type="bar"
                :options="options"
                :series="series"
                :xaxis="xaxis"
              ></apexchart>
            </i>
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
      gas: "",
      water: "",
      electro: "",
      za_dom: "",
      total: "",
      gas_actual: "",
      water_actual: "",
      electro_actual: "",
      za_dom_actual: "",
      total_actual: "",
      costs: [],
      date: [],
      options: {
        chart: {
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
      axios
        .post("http://127.0.0.1:8000/auth/jwt/refresh/", {
          refresh: localStorage.getItem("token"),
        })
        .then((response) => {
          console.log(response);
          localStorage.accessToken = response.data.access;
          axios
            .get(
              `http://127.0.0.1:8000/api/v1/user/statistics/invoice/${index}/`,
              {
                headers: {
                  Authorization: `Bearer ${localStorage.accessToken}`,
                },
              }
            )
            .then((response) => {
              this.gas = response.data[0].gasSumm;
              this.water = response.data[0].waterSumm;
              this.electro = response.data[0].electroSumm;
              this.za_dom =
                Number(response.data[0].repairSumm) +
                Number(response.data[0].trashSumm);
              this.total = response.data[0].total;
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
    get(index) {
      axios
        .post("http://127.0.0.1:8000/auth/jwt/refresh/", {
          refresh: localStorage.getItem("token"),
        })
        .then((response) => {
          // console.log(response);
          localStorage.accessToken = response.data.access;
          axios
            .get(`http://127.0.0.1:8000/api/v1/user/${index}`, {
              headers: {
                Authorization: `Bearer ${localStorage.accessToken}`,
              },
            })
            .then((response) => {
              const chart = this.$refs.chart.chart;
              chart.updateSeries([
                {
                  data: response.data.costs,
                },
              ]);

              chart.updateOptions({
                xaxis: {
                  categories: response.data.date,
                },
              });

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
      .post("http://127.0.0.1:8000/auth/jwt/refresh/", {
        refresh: localStorage.getItem("token"),
      })
      .then((response) => {
        console.log(response);
        localStorage.accessToken = response.data.access;
        axios
          .get("http://127.0.0.1:8000/api/v1/user/statistics/invoice/1/", {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          })
          .then((response) => {
            this.gas_actual = response.data[0].gasSumm;
            this.water_actual = response.data[0].waterSumm;
            this.electro_actual = response.data[0].electroSumm;
            this.za_dom_actual =
              Number(response.data[0].repairSumm) +
              Number(response.data[0].trashSumm);
            this.total_actual = response.data[0].total;
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
.container-2 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
}

.invoice-2 {
  border: 2px solid #333;
  padding: 20px;
  border-radius: 10px;
  width: 500px;
  text-align: center;
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
</style>