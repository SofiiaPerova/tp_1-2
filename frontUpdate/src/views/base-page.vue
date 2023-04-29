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
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav me-auto mb-2 mb-lg-0">
            <router-link to="/" class="nav-link active">Главная</router-link>
            <router-link to="/admin" class="nav-link active">Админка</router-link>
          </div>
          <div class="navbar-nav">
            <router-link to="/authorization" class="nav-link">Вход</router-link>
            <router-link to="/register" class="nav-link"
              >Регистрация</router-link
            >
          </div>
        </div>
      </div>
    </nav>
    <div
      style="
        background-position: center center;
        background-size: 30%;
        background-repeat: no-repeat;
        background-image: url('logo.jpg');
        height: 35%;
      "
    ></div>
    <div
      class="container-fluid row gy-5"
      style="display: grid; margin-right: auto; margin-left: auto"
    >
      <h1 style="justify-self: center">Управляющая компания</h1>
      <div>
        <h3>О нас</h3>
        <p>
          Управляющая компания занимается содержанием и ремонтом общего
          имущества, управлением им, обеспечивает исправность инженерных систем
          и конструкций дома, осуществляет предоставление качественных
          коммунальных услуг.
        </p>
      </div>
      <div>
        <h3>Часто задаваемые вопросы</h3>
        <div class="accordion accordion-flush" id="accordionFlushExample">
          <div class="accordion-item">
            <h2 class="accordion-header" id="flush-headingOne">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#flush-collapseOne"
                aria-expanded="false"
                aria-controls="flush-collapseOne"
              >
                Вопрос 1
              </button>
            </h2>
            <div
              id="flush-collapseOne"
              class="accordion-collapse collapse"
              aria-labelledby="flush-headingOne"
            >
              <div class="accordion-body">...</div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="flush-headingTwo">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#flush-collapseTwo"
                aria-expanded="false"
                aria-controls="flush-collapseTwo"
              >
                Вопрос 2
              </button>
            </h2>
            <div
              id="flush-collapseTwo"
              class="accordion-collapse collapse"
              aria-labelledby="flush-headingTwo"
            >
              <div class="accordion-body">...</div>
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
export default {
  mounted() {
    if (localStorage.token) {
      this.$router.push("/personal_account");
    }
  },
};
</script>

<style></style>