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

        <i-collapsible variant="light">
          <i-collapsible-item title="Показания каких счетчиков я могу внести?">
            <a
              >Внесение показаний проводится по счетчикам воды, газа и
              электроэнергии.</a
            >
          </i-collapsible-item>
          <i-collapsible-item title="Я забыл пароль. Как мне его восстановить?">
            <a
              >Если вы забыли пароль, вы можете перейти на страницу авторизации
              и нажать кнопку "Забыл пароль". После этого вам предложат ввести
              почту, после чего на нее будет отправлена ссылка для смены
              пароля.</a
            >
          </i-collapsible-item>
          <i-collapsible-item
            title="У меня есть предложения для новых функций сайта, куда мне написать по этмоу поводу?"
          >
            <a
              >Если у вас есть пожелания по функционалу сайта вы всегда можете
              написать нам на электронную почту или позвонить по номеру
              телефона. Вся контактная информация указана внизу страницы.</a
            >
          </i-collapsible-item>
        </i-collapsible>
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
export default {
  mounted() {
    if (localStorage.token) {
      this.$router.push("/personal_account");
    }
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