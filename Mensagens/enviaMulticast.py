import socket
import struct

# Criação do socket de envio
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Configuração do TTL
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Configuração do endereço e porta multicast
multicast_group = ('224.0.0.1', 10000)

while KeyboardInterrupt:
    # Dados a serem enviados
    message = input('Enter message to send: ').encode()

    try:
        # Envio de dados
        sent = sock.sendto(message, multicast_group)
    finally:
        print('Message sent.')