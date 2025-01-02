import requests

def buscar_cotacao(origem,destino):

    buscar = f"https://economia.awesomeapi.com.br/json/last/{origem}-{destino}"
    requisicao = requests.get(buscar)
    cotacao = requisicao.json()[f"{origem}{destino}"]["bid"]
    return cotacao