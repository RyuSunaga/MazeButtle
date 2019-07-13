from MazeClient import MazeClient

'''
mazefieldから呼び出すクラスです。
ユーザがコマンドを入力した後、イベント処理に入るのですが、
mainloop()から抜け出してサーバにデータを送信する方法がわからないので
このようなクラスを作りmainloop()に入ってからのサーバとの通信処理を実現することにしました。by nojima
'''
HOST = '127.0.0.1'
PORT = 50000
BACKLOG = 10
BUFSIZE = 4096

class connection(object):

    def __init__(self):
        pass

    def all_act(self):
        mc = MazeClient(HOST, PORT, BACKLOG, BUFSIZE)
        mc.set_player_id()
        mc.set_player_hp()
        mc.set_ctsp()
        mc.send()
        mc.listen()
        mc.get_player_id()
        mc.get_player_hp()
