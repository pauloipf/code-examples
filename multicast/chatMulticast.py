import socket
import struct
import threading

# Criação do socket de recepção
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Configuração do TTL
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Vinculação ao endereço do servidor
server_address = ('', 10000)
sock.bind(server_address)

# Participação no grupo multicast
multicast_group = '224.0.0.1'
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print('CHAT MULTICAST')

name = input('Enter your name: ')

# Função para receber mensagens
def receive_messages():
    while True:
        data, address = sock.recvfrom(1024)
        print(f'from {address}: {data.decode()}')

# Criação e início da thread para receber mensagens
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()
login = sock.sendto(f'{name} has joined the chat'.encode(), (multicast_group, 10000))


try:
    while True:
        # Dados a serem enviados
        message = input('Message ').encode()
        # Envio de dados
        sent = sock.sendto(message, (multicast_group, 10000))
except KeyboardInterrupt:
    print("Chat terminated.")
    sock.close()