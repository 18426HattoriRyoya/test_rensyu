import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #サーバを指定
    s.connect(('10.40.2.27', 50007))
    #メッセージを送る
    s.sendall(b'hello world')
    #ネットワークのバッファサイズは1024。サーバの文字列を取得
    data = s.recv(1024)
    print(repr(data))