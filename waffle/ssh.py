import getpass
from spur import SshShell, ssh

class SSHConn(object):
    def __init__(self, host, user='ubuntu', port=22, keyfile=None, timeout=5):
        self.host = host
        self.user = user
        self.port = int(port)
        self.keyfile = keyfile
        self.password = None

#        if not self.keyfile:
#            self.password = getpass.getpass("Password for %s" % host)

        self.shell = SshShell(
            hostname=self.host,
            port=self.port,
            username=self.user,
            connect_timeout=timeout,
            missing_host_key=ssh.MissingHostKey.accept)

