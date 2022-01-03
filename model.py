import peewee

db = peewee.SqliteDatabase("todo_app.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Card(BaseModel):
    id = peewee.CharField(primary_key=True, unique=True)
    name = peewee.CharField()


class Item(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField()
    completed = peewee.BooleanField(default=False)
    card = peewee.ForeignKeyField(Card, backref='items')
