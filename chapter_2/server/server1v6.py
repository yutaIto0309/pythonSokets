'''
IPv6によるサーバソケットの利用法を示すプログラム
'''

#モジュールのインポート
import socket
import datetime

#グローバル変数
PORT = 50000    #ポート番号

#メイン実行部
#ソケットの作成
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#アドレスの設定
server.bind(("",PORT))
#接続の待受け
server.listen()

#クライアントへの対応処理
while True:
    client,addr = server.accept()
    msg = str(datetime.datetime.now())
    client.sendall(msg.encode("utf-8"))
    print(msg, "接続要求あり")
    print(client)
    client.close
