from MazeClient import ClientMain
from config import TEST

C_HOST = '127.0.0.1'
C_PORT = 50000
C_BACKLOG = 10
C_BUFSIZE = 4096

name = input("プレイヤーの名前を入力してください。")
ClientMain(name, C_HOST, C_PORT, C_BACKLOG, C_BUFSIZE)
