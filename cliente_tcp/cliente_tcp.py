import socket  # biblioteca socket faz o relacioanmento da placa de rede com o SO
import sys     # fornece o acesso a algumas variáveis e funçoes q tem intereçã com o interpretador python

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("a conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()
    print("socket criado com sucesso")

    HostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("cliente TCP conectado com sucesso no host" + HostAlvo + " e na porta " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no host: " + HostAlvo + " - porta:" + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()
if __name__ == "__main__":
    main()