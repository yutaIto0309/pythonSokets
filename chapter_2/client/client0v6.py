'''
IPv6によるクライアントソケットの利用法を示すプログラム
'''

#モジュールのインポート
import socket

#グローバル変数
HOST = "localhost"
#HOST = "::1"
PORT = 50000
BUFSIZE = 4096

#メイン実行部
#ソケットの作成
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#サーバとの接続
client.connect((HOST, PORT))
#サーバーからのメッセージ受信
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
#コネクションのクローズ
client.close()