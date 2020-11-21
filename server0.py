# -*- coding: utf-8 -*-
"""
server0.py
Pythonによるサーバソケットの利用法を示す例題
50000番ポートで接続を待ち受けてメッセージを返す
"""

import socket

PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))
server.listen()

client, addr = server.accept()
client.sendall(b"Hi, nice to meet you!\n")
print(client, addr)
client.close()
server.close()
