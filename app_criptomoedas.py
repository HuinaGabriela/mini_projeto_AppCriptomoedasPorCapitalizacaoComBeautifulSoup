# Dicionario chamado moedas que me diz o preco da criptomoedas como bitcoin e outras moedas
# a variacao em 1 hora
# a variacao em 24 horas
# a variação em 7 dias
# é mesmo formato de uma app de criptomoeda,conecta com um site, lê as informações, organiza em formato que de para ler

from bs4 import BeautifulSoup
import requests
import re

# conectar com o site
link = "https://coinmarketcap.com/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())


tbody = site.find("tbody")
linhas = tbody.find_all("tr")
#print(linhas[0].text)

moedas = {}
for linha in linhas:
    try:
        nome = linha.find(class_="iPbTJf").text
        #print(nome)
        codigo = linha.find(class_="coin-item-symbol").text
        #print(codigo)
        valores = linha.find_all(string=re.compile("\\$"))
        preco = valores[0]
        percentuais = linha.find_all(string=re.compile("%"))
        
        for i, percentual in enumerate(percentuais): # mostra valor em queda 
            if "ivvJzO" in percentual.parent["class"]: # quando ta negativo
                percentuais[i] = "-" + str(percentual)

        #print(percentuais)
        var_1h = percentuais[0]
        var_24h = percentuais[1]
        var_7d = percentuais[2]
        
        market_cap = valores[2]
        volume = valores[3]
        dic = {"nome": nome, "codigo": codigo, "preco": preco, "market_cap": market_cap, "volume": volume,
              "var_1h": var_1h, "var_24h": var_24h, "var_7d": var_7d}
        moedas[nome] = dic
    except AttributeError:
        break
print(moedas)
