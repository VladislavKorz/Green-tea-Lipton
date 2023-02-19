<br/>
<p align="center">

<p align="center">
  <a href="https://github.com/VladislavKorz/Green-tea-Lipton">
    <img src="https://sun9-79.userapi.com/impg/O5ZAUMnI7j5wmsipnFJ3BCLI5uvzHfLSjHoCww/B58ZB2n_cEc.jpg?size=2048x2048&quality=96&sign=6320979adf8f8a5a882ff1bf84101e8f&type=album" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Readme file
</h3>

  <p align="center">
    Файл, содержащий информацию о сервисе
    <br/>
    <br/>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/VladislavKorz/Green-tea-Lipton?color=dark-green) 

## Содержание

* [Что реализовано](#about-the-project)
* [Сделано при помощи](#built-with)
* [Доступ к системе](#getting-started)
* [Установка и запуск](#prerequisites)

## Что реализовано
[Ссылка на проект](https://rm.qycode.ru)

1. Dashboard для Руководителя (Приветствие специалиста / Блок с информацией о Росмолодежь )
2. Dashboard для HR-специалиста (Приветствие специалиста / Блок с информацией о Росмолодежь )
3. Dashboard для Стажера (Приветствие стажера / Блок с информацией о Росмолодежь / Информация о процессе обучения и уведомления / календарь с задачами по стажировке)
4. Карта уровней для стажера с отображением всех чек поинтов (Выполнено - зеленый, Не выполнено - фиолетовый)
5. Конструктор уровней для HR-ов, возможность добавить/удалить/изменить/переместить уровень, отслеживать движение стажеров по уровням
6. Профиль пользователя с основной информацией и полученных достижениях
7. Страниц контактов компании с группировкой по своему отделу / руководителям и возможность сразу отправить им сообщения в мессенджеры
8. База знаний с возможностью добавить запись/документ для отдельного отдела или сразу всех
9. Блок FAQ
10. Поиск по базе знаний и FAQ
11. Возможность для HR специалиста создавать и настраивать уведомления
12. Рассылка уведомлений через телеграм бота и на почту
13. Обратная связь между стажером, hr-ом, руководителем, разработчиками платформы
14. Рейтинг стажеров по кол-ву выполненных задач
15. Удобная адаптация под мобильные версии устройств
16. Новости для отделов с инфомрацией о самом важном

## Сделано при помощи

BackEnd проекта реализован на django с дополнительными библиотеками (Перечень библиотек и их версии доступны в файле requirements.txt)
FrontEnd проекта реализован при использовании фреймворка bootstrap, и языков: html, css, js
В демо-проекте для более легкого развертывания используется база данных Sqlite3, в product-версии база данных PostgreSQL

## Доступ к системе


Для доступа к сайту используются следующие аккаунты: Руководитель: Логин: root Пароль: 1111

HR Специалист: Логин: root Пароль: 1111

Стажер: Логин: root Пароль: 1111

## Установка и запуск

Открыть VScode

Создать папку, в котором будут храниться необходимые файлы для запуска локального хостинга

Открыть терминал

Необходимо склоннировать репозиторий в ранее созданную папку по ссылке
Ввести в терминал команду
git clone https://github.com/VladislavKorz/Green-tea-Lipton.git
Нажать Ввод

Ввести в терминал команду
cd .\Green-tea-Lipton\sites\
Нажать Ввод

Ввести в терминал команду
cd ..
Нажать Ввод

Ввести в терминал команду
pip install -r requirements.txt
Нажать Ввод

Необходимо подождать окончания загрузки

Ввести в терминал команду 
cd sites
Нажать Ввод

Ввести в терминал команду 
python manage.py runserver
Нажать Ввод

В терминале в строке отобразится "Starting development server at"
Необходимо зажать клавишу Control и кликнуть ЛКМ по адресу в этой строке, который будет в формате "http://1**.*.*.*:8000/"

В браузере откроется сайт на локальном хостинге

Приятного пользования

[Ссылка на проект](https://rm.qycode.ru)



