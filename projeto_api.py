import requests
import os
import pprint
from dotenv import load_dotenv

load_dotenv() #carregas as variáveis de ambiente que criei

link_api="http://api.weatherapi.com/v1/current.json"
link_api2="http://api.weatherapi.com/v1/forecast.json"

chave_api = os.getenv('API_KEY')

dias_previsao = int(input("digite quantos dias de previsão você quer de 1 a 5:"))

parameters ={
    "key": chave_api,
    "q": "Teresina",
    "lang": "pt"
}

parameters2 ={
    "key": chave_api,
    "q": "Teresina",
    "lang": "pt",
    "days": dias_previsao
}

resultado_api = requests.get(link_api,params=parameters)

if resultado_api.status_code==200:
    dados_requisicao=resultado_api.json()
    temperatura = dados_requisicao['current']['temp_c']
    descricao = dados_requisicao['current']['condition']['text']
    cidade = dados_requisicao['location']['name']
    estado = dados_requisicao['location']['region']
    #pprint.pprint(dados_requisicao)
    print(temperatura)
    print(descricao)
    print(cidade)
    print(estado)
    
resultado_previsao = requests.get(link_api2,params=parameters2)

if resultado_previsao.status_code==200:
    dados_requisicao_dois=resultado_previsao.json()
    #pprint.pprint(dados_requisicao_dois)
    
    
    print(f"\n{'='*50}")
    print(f"=== PREVISÃO PARA {dias_previsao} DIAS EM {cidade} ===")
    print(f"{'='*50}")
    
    for i, dia in enumerate(dados_requisicao_dois['forecast']['forecastday']):
        print(f"\n📅 DIA {i+1} ({dia['date']}):")
        previsao_max = dia['day']['maxtemp_c']
        previsao_min = dia['day']['mintemp_c']
        condicao = dia['day']['condition']['text']
        
        print(f"   ☀️  Temperatura máxima: {previsao_max}°C")
        print(f"   ❄️  Temperatura mínima: {previsao_min}°C")
        print(f"   📝 Condição: {condicao}")
        print(f"\n{'='*50}")
    
    
else:
    print(f"Erro na previsão: {resultado_previsao.status_code}")   
    
    
