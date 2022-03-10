import os #importa modulo ou biblioteca OS (integra com os programas
# e recursos do SO

print("#" * 60) #imprime # 60 vezes

# criação de variavel que vai receber do usuario um ip
ip_ou_host = input("Digite o Ip ou Host a ser verificado: ")
print("-" * 60)
# chama system da biblioteca os - comando ping
# -n -num de pacotes que serao 6 {}
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 60)