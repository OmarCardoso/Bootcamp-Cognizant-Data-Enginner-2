from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebe requisicao http do site...
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
#print(soup.prettify())
#transoforma a estrutura html em string e o print vai exiber o html

#temperatura = soup.find("span", class_="variables-border-identifier -rain -fluid _height-60-perc _margin-t-5 _margin-r-5">)
#print(temperatura.string)

print(soup.title.string)