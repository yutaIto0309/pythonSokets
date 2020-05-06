'''
ホスト名をIPアドレスに変換するプログラム
'''

#モジュールのインポート
import socket

#メイン実行部
#繰り返し処理
while True:
    try:
        hostname = input("ホスト名を入力(qで終了)")
        if hostname == "q":
            break
        print(socket.gethostbyname(hostname))
    except:
        print("変換できませんでした")

