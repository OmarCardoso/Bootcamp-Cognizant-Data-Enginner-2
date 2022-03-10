import ipaddress

ip = "192.168.0.0/4"

# endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(rede)