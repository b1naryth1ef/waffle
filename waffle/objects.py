from waffle.ssh import SSHConn

class NodeMixin(object):
    def get_ssh_conn(self):
        return SSHConn(self.host, user=self.user, port=self.port)

    def bootstrap(self):
        ssh = self.get_ssh_conn()
        print ssh.shell.run(["hostname"])
        pass
