# Mishal Alajmi
# Date: 01/04/2021
# 
# This tool transfers large number of file over the network using sockets

import sys,os, os.path
import socket
# import tqdm


class Server:
    def __init__(self, HOSTNAME, PORT, BUFFER_SIZE):
        self.HOSTNAME = HOSTNAME
        self.PORT = PORT
        self.BUFFER_SIZE = BUFFER_SIZE
    
    def init_connection(self):
        # Create TCP socket
        s = socket.socket()
        # bind the socket to our target
        s.bind((self.HOSTNAME, self.PORT))
        # Accept 5 connections before refusing new ones
        s.listen(5)
        print(f"[*] Listening on: {self.HOSTNAME}:{self.PORT}")
        # accept any connection if there is any
        client_socket, address = s.accept()
        # if below code is executed, that means the sender is connected
        print(f"[+] {address} is connected")

        return s, client_socket

    def receive_files(self, server_socket, client_socket):
        # receive file metadata via client socket
        received = client_socket.recv(self.BUFFER_SIZE).decode()
        filename, filesize = received.split(' ')
        # remove abs path
        filename = os.path.basename(filename)
        # convert to int
        filesize = int(filesize)
        # init progress bar
        # prg_bar = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B",unit_scale=TRUE, unit_divisor=1024)

        with open(filename, "wb") as f:
            while True:
                # Read BUFFER_SIZE from the socket
                bytes_read = client_socket.recv(self.BUFFER_SIZE)
                if not bytes_read:
                    # nothing is received
                    break
                f.write(bytes_read)
                # prg_bar.update(len(bytes_read))
        # close client socket
        client_socket.close()
        # close server socket
        server_socket.close()
    

        

