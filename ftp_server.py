from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import MultiprocessFTPServer
import os

local = os.getcwd()
authorizer = DummyAuthorizer()
authorizer.add_user('user', '12345', '/home/adriandersonlira', perm='elradfmw')
authorizer.add_anonymous('/home/adriandersonlira', perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer

server = MultiprocessFTPServer(('127.0.0.1', 1026), handler)
server.serve_forever()
