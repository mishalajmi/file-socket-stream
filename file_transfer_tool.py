from server import Server
from client import Client
import argparse

parser = argparse.ArgumentParser("Welcome to the simple multi-threaded file transfer tool")
parser.add_argument('-m','--mode',metavar='mode',type=str,nargs='+',default='server',required=True)
parser.add_argument('--ip',metavar='ip',type=str,nargs=1,required=True)
parser.add_argument('-p','--port',metavar='port',type=int,nargs='+', required=True)
parser.add_argument('-t','--threads',metavar='threads',type=int,nargs='+',default=1,required=True)
parser.add_argument('-f','--file',metavar='file',type=str,nargs='+',default=1,required=True)
# TODO add more arguments
# Init parser & arguments
args = parser.parse_args()


if __name__ == '__main__':
    print(f"Running in {args.mode[0]} mode...ip: {args.ip[0]}...port: {args.port[0]}...num of threads: {args.threads[0]}")
    server = Server(args.ip,args.port,args.mode,args.threads,args.file[0])
    server.count_files_dir(server.get_full_path())