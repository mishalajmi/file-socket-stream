# Mishal Alajmi
# Date: 01/04/2021
# 
# This tool transfers large number of file over the network using sockets

import sys,os, os.path
import socket
import threading


class Server:
    def __init__(self,HOSTNAME,PORT,MODE="",NUM_THREADS=1,FILEPATH=""):
        self.HOSTNAME = HOSTNAME or socket.gethostbyname('0.0.0.0')
        self.PORT = PORT
        self.MODE = MODE
        self.NUM_THREADS = NUM_THREADS
        self.FILEPATH = FILEPATH
        self.T_POOL = [self.NUM_THREADS]
        # self.JOB_QUEUE = 
    
    def get_filepath(self):
        """
        @input none
        @op retrieves the full path of where the file resides
        @retrun full path as string
        """
        try:
            full_path = os.path.abspath(self.FILEPATH)
            print(f"Counting number of files in: {full_path}")
        except Exception as e:
            raise SystemExit(f"Could not complete operation: {e}")
            
    
    def est_connection(self):
        """
        @input none
        @op establishes a connection with the provided info
        @return socket
        """
        try:
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                s.connect((self.HOSTNAME,self.PORT))
        except socket.error as msg:
            print(f"Caught exception: {msg}")

