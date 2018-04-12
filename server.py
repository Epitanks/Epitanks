# chat_server.py
 
import sys
import socket
import select

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    players = ""
    tanks = ['Assets/PNG/tank_red.png', 'Assets/PNG/tank_green.png',
    'Assets/PNG/tank_dark.png', 'Assets/PNG/tank_blue.png']
    i = 0
    print "Chat server started on port " + str(PORT)
    while 1:
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0) 
        for sock in ready_to_read:
             # a new connection request received
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                players += broadcast(server_socket, sockfd, "%s:%s#" % addr + tanks[i] + "#" + str(i * 100) + "#10" + '#\n')
                sockfd.send(players)
                i += 1
                print(players)
            # a message from a client, not a new connection
            else: 
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                       # print(data)
                        broadcast(server_socket, sock, data)  
                    else:
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()

def broadcast(server_socket, sock, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
    return message
 
if __name__ == "__main__":

    sys.exit(chat_server())  