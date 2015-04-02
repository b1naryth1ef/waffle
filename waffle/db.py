import os
from peewee import *

from waffle.objects import NodeMixin

database = SqliteDatabase("waffle.db")

class BaseModel(Model):
    class Meta:
        database = database

class Cluster(BaseModel):
    """
    Represents a cluster
    """

    name = CharField(unique=True)

    @staticmethod
    def get_current():
        if os.getenv("CLUSTER"):
            return Cluster.select().where(Cluster.name == os.getenv("CLUSTER")).get()
        return Cluster.select().order_by(Cluster.id).get()

class Node(BaseModel, NodeMixin):
    """
    Represents a phsyical node that will host containers
    """
    cluster = ForeignKeyField(Cluster)

    name = CharField(unique=True)
    host = CharField(unique=True)
    port = IntegerField(default=22)
    user = CharField()

class Container(BaseModel):
    """
    Represents a container in our cluster
    """
    cluster = ForeignKeyField(Cluster)
    node = ForeignKeyField(Node)

    name = CharField(unique=True)
    state = IntegerField()


MODELS = [Cluster, Node, Container]

def create_db():
    database.connect()
    database.create_tables(MODELS, True)
create_db()

