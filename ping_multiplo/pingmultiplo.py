import os
import time

with open('hosts.txt') as file: # abre o arquivo como file
    dump = file.read() #Le o arquivo
    dump = dump.splitlines()

    for ip in dump:
        print('verificando o ip:', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)

