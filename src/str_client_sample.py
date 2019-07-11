'''
Created on 2019/04/25

@author: masan
'''
#必ずインポート
import socket
from packet import ClientToServerPacket,ServerToClientPacket
import pickle


#接続先ホストの名前。ドメイン込み（あるいはIPアドレス）
HOST='127.0.0.1'#ローカルホスト名。自分自身
#接続先ホストのポート番号
PORT=50000#50000~55000で選択
#ソケットから送受信するデータのバッファサイズ
BUFSIZE=4069

#ソケットの作成
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:#例外処理を入れたほうが良い
    #サーバへの接続
    sock.connect((HOST,PORT))
    '''
    #バイトコード化してデータを送信
    ctsp=ClientToServerPacket()
    ctsp.set_next_command
    ctsp.set_player_id
    '''

    dic='{1:"a",2:"b"}'

    sock.send(dic.encode())
    #データを受信
    receive_msg=sock.recv(BUFSIZE)
    print(receive_msg)
finally:
    #接続のクローズ
    sock.close()#基本的には最後に閉じる
print('end')
