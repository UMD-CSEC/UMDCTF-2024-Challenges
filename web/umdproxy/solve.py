import server_socket

server_sock = server_socket.server_socket(server_socket.AF_INET, server_socket.SOCK_STREAM)
server_sock.bind(("", 8888))
server_sock.listen()

client_server_sock, _ = server_sock.accept()
