import uuid

from waffle.db import Cluster, Node
from waffle.util import generate_name
from waffle.cli import command

@command()
def create_cluster(args, name=None):
    """
    Create a new cluster
    """
    try:
        cluster = Cluster.create(name=name or generate_name())
    except Exception as e:
        print("Error creating cluster: %s" % e)
        return False
    print("Cluster #%s aka %s created!" % (cluster.id, cluster.name))

@command()
def bootstrap(args, name=None, host=None, port=22, user='ubuntu'):
    """
    Adds and configures a new physical host to the cluster
    """
    cluster = Cluster.get_current()
    node = Node.create(
        cluster=cluster,
        name=name or generate_name(),
        host=host,
        port=port,
        user=user)

    print("Added node #%s aka %s to the cluster" % (node.id, node.name))
    print("Bootstraping node #%s" % node.id)

    node.bootstrap()

@command()
def create(args, name=None, image="ubuntu"):
    """
    Creates a new managed LXC container
    """
    name = name or generate_name()
    print("Attempting to create container %s" % (name, ))
    cluster = Cluster.get_current()
    pass

@command()
def create_temp(args, image="ubuntu"):
    """
    Create a temporary container without a persistant backing store.
    """
    pass

