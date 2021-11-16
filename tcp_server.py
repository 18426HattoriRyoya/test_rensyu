import socket
# AF = IPv4という意味
# TCP/IPの場合はSOCK_STREAMを使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      #IPアドレスとポートを指定
    s.bind(('0.0.0.0', 50007))
    #接続
    s.listen(1)
    # connectionするまで待つ
    while True:
        #誰かがアクセスしたらコネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            while True:
        #データ受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {},　addr: {}'.format(data, addr))
                #クライアントにデータを返す
                conn.sendall(b'Received: ' + data)