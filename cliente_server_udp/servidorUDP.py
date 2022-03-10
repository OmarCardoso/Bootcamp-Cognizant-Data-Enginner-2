import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('socket criado com sucesso!!!')

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\nServidor: Olá cliente e ai blz?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)