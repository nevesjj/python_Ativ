import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json() 
print('1. Dólar')
print('2. Euro')
print('3. Bitcoin')
print('4. Sair')

while True:

   opcao = int(input('Digite a opção desejada : ')) 
   if opcao == 1:
      valor = float(input('Digite o valor em real: ')) 
      cotacao_dolar = float(cotacoes['USDBRL']['bid'])
      total = valor / cotacao_dolar
      total = "{:.2f}".format(total)
      print('$',total)

   elif opcao == 2:
      valor = float(input('Digite o valor em real: ')) 
      cotacao_euro = float(cotacoes['EURBRL']['bid'])
      total = valor / cotacao_euro
      total = "{:.2f}".format(total)
      print('€',total)

   elif opcao == 3:
      valor = float(input('Digite o valor em real: ')) 
      cotacao_btc = float(cotacoes['BTCBRL']['bid'])
      total = valor / cotacao_btc 
      total = "{:.4f}".format(total)
      print('₿',total)

   elif opcao == 4:
      break


print('Você encerrou o programa')




   





