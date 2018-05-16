from peewee import *
from datetime import datetime

from type.entity import EntityIsDeleted
from entity._base import BaseModel

class Article (BaseModel):
    id = IntegerField(primary_key = True)
    isDeleted = IntegerField(default = EntityIsDeleted.no)
    title = CharField(max_length = 200, null = True, default = '')
    content = TextField(default = '', null = True)

    # TODO: 安装 playhouse 扩展支持 Postgres 特有字段.
    # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#ArrayField
    # tags = ArrayField()

    createAt = DateTimeField(default = datetime.now)
    lastUpdate = DateTimeField(default = datetime.now)
