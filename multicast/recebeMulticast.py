import socket
import struct

# Criação do socket de recepção
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Configuração de opções do socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Vinculação ao endereço do servidor
server_address = ('', 10000)
sock.bind(server_address)

# Participação no grupo multicast
multicast_group = '224.0.0.1'
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print('Waiting to receive message')

# Recebendo dados
while True:
    data, address = sock.recvfrom(1024)

    # print(f'Received {len(data)} bytes from {address}')
    print(f'Mensagem de {address}: {data.decode()}')