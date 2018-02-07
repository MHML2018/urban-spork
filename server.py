import socket
import threading

## Starting code from:
## https://gist.github.com/tuxmartin/e7c85f84153ba15576c5

bind_ip = '127.0.0.1'
bind_port = 5006

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

    print('Listening on ', bind_ip, bind_port)


    def handle_client_connection(client_socket):
        print("Listening for data")
        request = client_socket.recv(1024)
        print('Received', request)
        client_socket.send(b'ACK!')
        client_socket.close()

    while True:
        client_sock, address = server.accept()
        print('Accepted connection from', address[0], address[1])
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        )
        client_handler.start()
