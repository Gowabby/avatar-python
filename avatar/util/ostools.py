import os
import errno
import random
import socket

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise 
        
        
def get_random_free_port(interface = '0.0.0.0'):
    while True:
        port = random.randint(20000, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((interface, port))
            sock.close()
            return port
        except Exception as ex:
            raise ex
