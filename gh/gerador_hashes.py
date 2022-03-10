import hashlib

string = input('Digite o texto para ser gerada a hash: ')

menu = int(input('''###Menu - Escolha o tipo de Hash###
            1) MD5
            2) SHA1
            3) SHA 256
            4) SHA 512
            Digite o número do Hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A Hash md5 da String: ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A Hash sha1 da String: ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A Hash sha256 da String: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A Hash sha512 da String: ', string, 'é: ', resultado.hexdigest())
else:
    print('Digite uma opção válida')