'''
server0.pyプログラム
サーバソケットの利用法を示す例題プログラム
'''

#モジュールのインポート
import socket

#グローバル変数
PORT = 50000

#メイン実行部
#ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#アドレスの設定
server.bind(("",PORT))

#接続の待ち受け
server.listen()

#クライアントへの対応処理
client, addr = server.accept()
client.sendall(b"Hi! nice to meet you!\n")
client.close()
server.close()