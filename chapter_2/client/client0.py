'''
クライアントソケットの利用法を示す例題プログラム
'''

#モジュールのインポート
import socket

#グローバル変数
HOST = "localhost"  #接続先のホスト名
#HOST = "127.0.0.1"
PORT = 50000
BUFSIZE = 4096

#メイン実行部

#ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#サーバとの接続
client.connect((HOST, PORT))

#サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))

#コネクションのクローズ
client.close()