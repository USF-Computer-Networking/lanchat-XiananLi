# This file is simply help to access the server socket created
# at the specified IP address and port. After that, it will check
# whether the input comes from the server or from the client side,
# and help to redirect the ouput

import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print
    "IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

    sockets_list = [sys.stdin, server]

    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print
            message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()


# learned simple chat function through link:
# https://www.geeksforgeeks.org/simple-chat-room-using-python/
