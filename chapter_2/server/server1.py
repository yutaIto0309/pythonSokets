'''
サーバソケットの利用方を示す例題プログラム
'''

#モジュールのインポート
import socket
import datetime

#グローバル変数
PORT = 50000    #ポート番号

#メイン実行部
#ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#アドレスの設定
server.bind(("", PORT))

#接続待ち
server.listen()

#クライアントへの対応処理
while True:
    client, addr = server.accept()
    msg = str(datetime.datetime.now())
    client.sendall(msg.encode("UTF-8"))
    print(msg, "接続要求あり")
    print(client)
    client.close()

