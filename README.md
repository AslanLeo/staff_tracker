Репозиторий staff_controller
Установка (для пользователей операционных систем семейства MacOs/Linux):

1.Открыть терминал или консоль и перейти в нужную Вам директорию
2.Прописать команду git clone git@github.com:AslanLeo/staff_controller.git

3.Если Вы используете https, то: git clone https://github.com/AslanLeo/staff_controller.git

4.Прописать следующие команды:


python3 -m venv ДиректорияВиртуальногоОкружения
source ДиректорияВиртуальногоОкружения/bin/activate
Перейти в директорию staff_controller

pip install -r requirements.txt
python manage.py migrate


5.Запустить сервер - python manage.py runserver