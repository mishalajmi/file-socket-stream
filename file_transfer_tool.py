from server import Server
from client import Client
import argparse

parser = argparse.ArgumentParser("Welcome to the simple multi-threaded file transfer tool")
parser.add_argument('-m','--mode',metavar='mode',type=str,nargs='+',default='server',required=True)
parser.add_argument('--ip',metavar='ip',type=str,nargs=1,required=True)
parser.add_argument('-p','--port',metavar='port',type=int,nargs='+', required=True)
parser.add_argument('-f','--file',metavar='file',type=str,nargs='+',default=1,required=True)
# TODO add more arguments
# Init parser & arguments
args = parser.parse_args()


if __name__ == '__main__':

    if args.mode[0] == "server":
        print(f"[+]Running in {args.mode[0]} mode")
        server = Server(args.ip[0],args.port[0],500)
        s_sock, c_sock = server.init_connection()
        server.receive_files(s_sock, c_sock)
    elif args.mode[0] == "client":
        print(f"[+]Running in {args.mode[0]} mode")
        client = Client(args.ip[0],args.port[0],500,args.file[0])
        client.est_connection()
