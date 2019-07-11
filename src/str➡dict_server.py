#--- encoding UTF-8 ---

import socket
import select
from packet import ServerToClientPacket, ClientToServerPacket
import ast

def send_to(sock, msg):
    try:
        sock.send(msg.encode())
        return True
    except:
        sock.close()
        return False

def broadcast(socklist, msg):
    for sock in socklist:
        if not send_to(sock, msg):
            socklist.remove(sock)


HOST = '127.0.0.1'
PORT = 50000
BACKLOG = 10
BUFSIZE = 4096

#ソケットを作成
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("sockete is created")
try:
    server_sock.bind((HOST, PORT))
    print("socket bind")
    server_sock.listen(BACKLOG)
    print("socket listen")
    sock_list = [server_sock]
    #クライアントのソケットをポートで管理するために辞書型でソケットを保存する
    client_sock_table={}
    while True:
        r_ready_sockets, w_ready_sockets, e_ready_sockets = select.select(sock_list, [], [])
        for sock in r_ready_sockets:
            if sock == server_sock:
                conn, address = sock.accept()
                sock_list.append(conn)
                #ポートをキーとして保存する
                client_sock_table[address[1]]=conn
                #誰かからの接続があったことを全員に通知する
                sock_list.remove(server_sock)
                broadcast(sock_list, "ポート" + str(address[1]) + "番のユーザーが接続しました")
                sock_list.append(server_sock)
                print(str(address) + "is connected")
            else:
                try:
                    b_msg = conn.recv(BUFSIZE)
                    msg = b_msg.decode('utf-8')
                    print('received messege:' + msg)
                    dic=ast.literal_eval(msg)
                    print(type(dic))
                    print(dic[1])
                    if len(msg) == 0:
                        sock.close()
                        sock_list.remove(sock)
                    else:
                        #client_sock_tableから送信者のポートを調べる
                        #辞書型のキーと値をfor文で順に参照する
                        sender_port=None
                        for key,val in client_sock_table.items():
                            if val==sock:
                                sender_port=key
                                break
                            if sender_port is not None:
                                sock_list.remove(server_sock)
                                broadcast(sock_list, str(sender_port) + ","+ msg)
                                sock_list.append(server_sock)
                except:
                    sock.close()
                    sock_list.remove(sock)
                    sock_list.remove(server_sock)
                    broadcast(sock_list, "someone disconnected")
                    sock_list.append(server_sock)

except Exception as e:
    print("Exception")
    print(e)
    server_sock.close()
