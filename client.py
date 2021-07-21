import os, math
import socket
# import tqdm

class Client:
    def __init__(self, HOSTNAME, PORT, BUFFER_SIZE, FILENAME ):
        self.HOSTNAME = HOSTNAME or socket.gethostbyname('0.0.0.0')
        self.PORT = PORT
        self.BUFFER_SIZE = BUFFER_SIZE
        self.FILENAME = FILENAME

    
    def get_file_size(self):
        """
        @input none
        @op returns the size of the file
        @return size of the file as an int
        """
        try:
            return os.path.getsize(self.get_full_path())
        except Exception as e:
            raise SystemExit(f"Could not complete operation: {e}")
    
    def get_full_path(self):
        """
        @input none
        @op retrieves the full path of the directory that contains the file
        @retrun full path as string
        """
        try:
            return os.path.abspath(self.FILENAME)
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
    
    
    def stream_files(self, sock):
        #init progress bar
        # prg_bar = tqdm.tqdm(range(self.get_file_size(self.get_full_path(self.FILENAME))), unit="B", unit_scale=True, unit_divsior=1024)
        with open(self.get_full_path(),'rb') as f:
            bytes_read = f.read(self.BUFFER_SIZE)
            if not bytes_read:
                # Done transmitting
                return
            sock.sendall(bytes_read)
            # prg_bar.update(len(bytes_read))
        # end connection
        sock.close()

    
    def est_connection(self):
        """
        @input none
        @op establishes a connection with the provided info
        @return socket
        """
        try:
            file_size = math.ceil(self.get_file_size())
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                print(f"[+]connecting to {self.HOSTNAME}:{self.PORT}")
                s.connect((self.HOSTNAME,self.PORT))
                print(f"[+]Connected")
                # prime the server with file meta data
                s.send(f"{self.FILENAME} {file_size}".encode())
                print(f"[+]Sending file info from: {self.get_full_path()}")
                self.stream_files(s)
            return 

        except socket.error as msg:
            print(f"Caught exception: {msg}")



