import requests
api_key= "1d0d1cf008c52312335aba6c34e2a053"

while True:
    cidade = str(input('Digite o nome da cidade : '))
    api = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"
    requisicao = requests.get(api)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    temperatura = "{:.1f}".format(temperatura)
    print(descricao, f"= {temperatura} C°")
    opcao = int(input('1. Consultar nova cidade \n2. Finalizar consulta\n'))

    if opcao == 2: 
        print('Você finalizou o atendimento !!!')
        break


