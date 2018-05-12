# game_server.py
 
import sys
import socket
import select


class Server:
    def __init__(self):
        self.HOST = ''
        self.SOCKET_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = 9009
        self.states = ['WaitingRoom', 'Game']
        self.current_state = 'WaitingRoom'

    def game_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen(10)

        # add server socket object to the list of readable connections
        self.SOCKET_LIST.append(server_socket)

        players = ""
        tanks = ['Assets/PNG/tank_red.png', 'Assets/PNG/tank_green.png',
        'Assets/PNG/tank_dark.png', 'Assets/PNG/tank_blue.png']
        i = 1
        print "server started on port " + str(self.PORT)
        while self.current_state == self.states[0]:
            ready_to_read, ready_to_write, in_error = select.select(self.SOCKET_LIST, [], [], 0)
            for sock in ready_to_read:
                 # a new connection request received
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    self.SOCKET_LIST.append(sockfd)
                    print "Client (%s, %s) connected" % addr
                    players += self.broadcast(server_socket, sockfd, "%s:%s#" % addr + tanks[i] + "#" + str(i * 200) + "#100" + '#\n')
                    sockfd.send(players)
                    i += 1
                    print(players)
                # a message from a client, not a new connection
                else:
                    try:
                        data = sock.recv(self.RECV_BUFFER)
                        if data:
                            self.broadcast(server_socket, sock, data)
                        else:
                            if sock in self.SOCKET_LIST:
                                self.SOCKET_LIST.remove(sock)
                            self.broadcast(server_socket, sock, "$%s:%s$" % addr)
                    except:
                        self.broadcast(server_socket, sock, "$%s:%s$" % addr)
                        continue
        server_socket.close()

    def broadcast(self, server_socket, sock, message):
        for socket in self.SOCKET_LIST:
            if socket != server_socket and socket != sock:
                try:
                    socket.send(message)
                except:
                    socket.close()
                    if socket in self.SOCKET_LIST:
                        self.SOCKET_LIST.remove(socket)
        return message

    def isWaitingRoom(self):
        return self.current_state

if __name__ == "__main__":
    my_server = Server()
    sys.exit(my_server.game_server())