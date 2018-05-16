from peewee import *

db = PostgresqlDatabase('playground', user='postgres', host='127.0.0.1', port=5432)

# BaseModel, 指定连接的数据库.
class BaseModel(Model):
    class Meta:
        database = db # 指定数据库.
