# this file will try to establish a socket and combine it to an IP
# address and port specified by the user. It will stay open and receive
# connection requests, and will append respective socket object to a 
# list to keep track of active connection. Everytime one new user connects,
# it will creted a new thread for the new user, the thread will awaits a 
# message, and sends message to other users currently on the chat.


import socket
import select
import sys
from thread import *

# The argument AF_INET is the address domain of the sockets
# The argument SOCK_STREAM  is the data are read in the flow

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# check if the argument is valid
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()

# take the first argument as IP address
IP_address = str(sys.argv[1])

# take second argument as port number
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients = []

def clientthread(conn, addr):
    
    #send a message to the client 
    conn.send("Welcome to this chatroom!")
   
  while True:
            try:
                message = conn.recv(2048)
                if message:
    
                    print "<" + addr[0] + "> " + message
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send, conn)

                else:
                    remove(conn)

            except:
                continue
                
             
# using this function to broadcast the message to all the clients
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()

                remove(clients)
# using this function removes the object from the list
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:

    conn, addr = server.accept()

    list_of_clients.append(conn)

    print addr[0] + " connected"

    start_new_thread(clientthread,(conn,addr))    

conn.close()
server.close()


# learned simple chat function through link:
# https://www.geeksforgeeks.org/simple-chat-room-using-python/

