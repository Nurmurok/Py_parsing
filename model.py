from peewee import *

db = PostgresqlDatabase(
    database="Your databese",
    password="Your password",
    user="postgres",
    host="localhost",
    port=5432
)


class Data(Model):
 
    date_posted = CharField()
    price = CharField()
    currency=CharField()
    image=CharField()
   

    class Meta:
        database = db


db.connect()
db.create_tables([Data])



