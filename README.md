# Parser с помощью Python
### Информация о проекте
C веб-сайта необходимо собрать все объявления, включая пагинацию.

[3690 Fresh Listings | Browse Apartments & Condos for Sale or Rent in City of Toronto | Kijiji Classifieds](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273)

Из каждого объявления вам нужно набрать следующие пункты:

🖼 Изображение: сохранить только URL.
📆 Дата: сохранить в формате дд-мм-гггг.
💲 Валюта должна быть сохранена как отдельный атрибут.

## Требования:

### База данных - PostgreSQL
### ORM - peewee
### виртуальная среда - venv


### Выполните следующие действия:
```python
git clone "https://github.com/Nurmurok/parser.git"
cd parser
python -m venv venv
.\venv\Scripts\activate 
pip install -r requirments.txt
```

### Создайте свою базу данных, измените название и пароль от базы данных в файле model.py
```python
db = PostgresqlDatabase(
    database="Your databese",
    password="Your password",
    user="postgres",
    host="localhost",
    port=5432
)
```

### Начни парсить запустив файл main.py

```python
python main.py
```

