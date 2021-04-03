# Mishal Alajmi
# Date: 01/04/2021
# 
# This tool transfers large number of file over the network using sockets

import sys,os, os.path
import socket
import threading


class Server:
    def __init__(self,HOSTNAME,PORT,MODE="",NUM_THREADS=1,FILENAME=""):
        self.HOSTNAME = HOSTNAME or socket.gethostbyname('0.0.0.0')
        self.PORT = PORT
        self.MODE = MODE
        self.NUM_THREADS = NUM_THREADS
        self.FILENAME = FILENAME
        self.T_POOL = [self.NUM_THREADS]
        # self.JOB_QUEUE = 
    
    def get_full_path(self):
        """
        @input none
        @op retrieves the full path of the directory that contains the file
        @retrun full path as string
        """
        try:
            full_path = os.path.abspath(self.FILENAME).replace(f'/{self.FILENAME}','')
            print(f"Reading directory: {full_path}")
            return full_path
        except Exception as e:
            raise SystemExit(f"Could not complete operation: {e}")
    
    def count_files_dir(self,full_path):
        """
        @input full path of the file
        @op counts the number of files in the directory excluding the dir itself
        @returns number of files as int
        """
        try:
            num_files = len([name for name in os.listdir(full_path) if os.path.isfile(self.FILENAME)])
            print(f"Number of files in {full_path} is {num_files}")
            return num_files
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

