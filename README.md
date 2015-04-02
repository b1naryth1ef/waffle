# Waffle
Waffle is a simple toolchain for managing a distributed set of LXC containers across multiple linux machines. It was built as an alternative to things like mesos or terraform which require more complex infrastructure and setup to use.


## Setup Waffle
Waffle requires phsyical hosts to run containers on. To setup a node for waffle usage, you can run the waffle bootstrap command `waffle bootstrap host:hostname port:port user:username`. By default, the nodes name will be the hostname, this can be changed by passing the `name` paramater.

## Distributing State
By default, all waffle nodes know the full topology of the enviroment, and waffle commands for the cluster can be run by any node.

### Basic Usage

- Create a container: `waffle create name:test01 image:fedora`
- Create a temporary container: `waffle create-temp name:test01 image:fedora`
- List all containers: `waffle ls`
- Info for a specific container: `waffle info <ID or name>`
- Shell into a container: `waffle shell <ID or name>`
- List physical hosts: `waffle host ls`
- Migrate a container from one host to another: `waffle mv <ID or name> <new host ID or name>`

