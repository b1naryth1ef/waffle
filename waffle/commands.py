import uuid

from waffle.util import generate_name
from waffle.cli import command

@command()
def bootstrap(args, host=None, port=None, user=None):
    """
    Adds and configures a new physical host to the cluster
    """

@command()
def create(args, name=None, image="ubuntu"):
    """
    Creates a new managed LXC container
    """
    id = str(uuid.uuid4())
    name = name or generate_name()
    print("Attempting to create container %s (%s)" % (name, id))
    pass

@command()
def create_temp(args, image="ubuntu"):
    """
    Create a temporary container without a persistant backing store.
    """
    pass

