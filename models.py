from peewee import *

# database connection
db = SqliteDatabase("shopyoo.db")
class Inventory(Model):
    name = CharField(unique=True)
    price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = db



class User(Model):
    user_name = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Cart(Model):
    user = ForeignKeyField(User)
    item = ForeignKeyField(Inventory)
    quantity = IntegerField()

    class Meta:
        database = db



def create_tables():
    # create tables in sqlite db
    with db:
        db.create_tables([Inventory,User,Cart])
