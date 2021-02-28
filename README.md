# online_shop

Скопируйте проект командой: https://github.com/vlad1ee/online_shop.git или по SSH: git@github.com:vlad1ee/online_shop.git

Создайте виртуальное окружение: python3 -m venv venv и активируйте его: source venv/bin/activate.

На всякий случай обновите pip3 install --upgrade pip

Установите зависимости командой pip install -r requirements.txt. 

Затем, в настройках проекта, в файле settings.py вам нужно настроить базу данных (создать пользователя, указать его USERNAME и PASSWORD, создать базу данных и в 
зависимости от этого изменить NAME, PORT оставить без изменений).

Создайте миграции, находясь в одной директории с файлом manage.py: ./manage.py makemigrations, а затем мигрируйте: ./manage.py migrate. 

Создайте суперпользователя для доступа в административную панель командой: ./manage.py createsuperuser 

Находясь в одной директории с файлом manage.py запустите сервер на 8000 порту командой: ./manage.py runserver

Ниже приведен список url адресов:

/auth/users/ --- для регистрации по API (после регистрации приходит сообщение на вашу почту что-то вроде "http://localhost:8000/#/activate/Mw/ait4b3-4e7ed0b4a366db211994885095c195ba" и для того чтобы подтвердить личность нужно воспользоваться программой Postman и ввести значения где 'Mw' - это uid, а 'ait4b3-4e7ed0b4a366db211994885095c195ba' - это token и отправить POST-запрос после чего вы можете залогиниться под этим аккаунтом

/api/v1/user/<int:pk>/ -- для просмотра и редактирования своего профиля

/category/create/ -- для создания вложенных категорий

/category/product/create/ -- для создания товара
