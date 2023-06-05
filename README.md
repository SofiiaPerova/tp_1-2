# КоммУслуги
Приложение для сбора показаний счетчиков и выставление общего счета за предоставленные услуги.

Проект "Веб-приложение для сбора показаний индивидуальных приборов учёта в многоквартирных домах и выставление счетов за потреблённые услуги" упрощает процесс оплаты ЖКХ, предоставляя пользователям возможность делать это онланн и по единому лицевому счету. 


Особенновстямми проекты являются возможности не только формировать счет на оплату по введенным показаниям, но и просматривать как статистику потребления, так и статистику расходов. В статистике потребления пользователю выводится график показаний приборов по выбранной услуге. В статистике оплаты пользователю выводится квитанция, в которой указано сколько он заплатил за ту или иную слугу в выбранном месяце.

# Команда разработчиков
1. Кольцова Ирина
2. Перова София
3. Крылов Денис
# Сервисы
[Miro](https://miro.com/app/board/uXjVPhwKcxY=/?share_link_id=3595978674481)

[Figma - интерактивный прототип](https://www.figma.com/file/GgbEZk4ULs4jx0dbqQBhxD/Untitled?node-id=1%3A2&t=5dXsrv4S4VSqIxdC-1)

[Jira](https://tp-task-manager.atlassian.net/jira/software/projects/T12/boards/1)

# Документация
[Курсовой проект](https://github.com/SofiiaPerova/tp_1-2/blob/main/documents/%D0%9A%D1%83%D1%80%D1%81%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.pdf)

[ТЗ](https://github.com/SofiiaPerova/tp_1-2/blob/main/documents/%D0%A2%D0%97.docx)

[Диаграммы](https://github.com/SofiiaPerova/tp_1-2/tree/main/documents/diagrams)

# Видео
[Разбор серверной части](https://github.com/SofiiaPerova/tp_1-2/blob/main/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE/Back.mp4)

[Разбор клиентской части](https://github.com/SofiiaPerova/tp_1-2/blob/main/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE/Front.mp4)

[Разбор развертывания](https://github.com/SofiiaPerova/tp_1-2/blob/main/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE/%D0%A0%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D1%82%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.mp4)

[Презентация проекта](https://github.com/SofiiaPerova/tp_1-2/blob/main/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE/%D0%9F%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F.mp4)
[Демо сайта](https://github.com/SofiiaPerova/tp_1-2/blob/main/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE/%D0%94%D0%B5%D0%BC%D0%BE%20%D1%81%D0%B0%D0%B9%D1%82%D0%B0.mp4)

# Локальное развертывание
Для развертывания проекта на локальном сервере необходимо:
1. Склонировать ветку Develop.
2. Установить зависимости для vue.js командой nmp install.
3. Установить рависимости для python командой pip install -r requirements.txt
4. Настроить в ssetings.py параметры своей БД.
5. Провести миграции: python manage.py makemigrations и затем применить их 
python manage.py migrate
6. Запустить сервер командой python manage.py runserver.
7. Запустить клиент командой npm run serve.

# VPS-сервер
Сайт доступен по адресу : http://45.146.164.34:5000/
swagger: http://45.146.164.34:8080/swagger/

Аккаунт администратора:

admin@mail.ru

AdMiN333


Аккаунт пользователя:

user@mail.ru

UsEr3333
