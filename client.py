import sys, os
import socket
import threading

class Client:
    def __init__(self, HOSTNAME, PORT, NUM_OF_THREADS):
        self.HOSTNAME = HOSTNAME
        self.PORT = PORT
        self.NUM_OF_THREADS = NUM_OF_THREADS
    
    def get_filename_path(self, filename):
        with open(file=filename) as f:
            f.buffer.read(500)
            

