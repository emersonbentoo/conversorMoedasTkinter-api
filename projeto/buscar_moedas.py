import xmltodict

def nomes_moedas():
    with open(r"C:\Users\emers\OneDrive\Área de Trabalho\PROJETOS\CONVERSOR_MOEDAS\moedas.xml", "rb" ) as arquivos_moedas:
        dic_moedas= xmltodict.parse(arquivos_moedas)

    moedas = dic_moedas["xml"]
    return moedas

def conversao_disponiveis():
    with  open(r"C:\Users\emers\OneDrive\Área de Trabalho\PROJETOS\CONVERSOR_MOEDAS\conversoes.xml","rb") as arquivo_conversao :
        dic_conversoes = xmltodict.parse(arquivo_conversao)

    conversao = dic_conversoes["xml"]
    dic_conversao_disponiveis= {}
    for par_conversao in conversao:
        moeda_origem, moeda_destino = par_conversao.split("-")
        if moeda_origem in dic_conversao_disponiveis:
            dic_conversao_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dic_conversao_disponiveis[moeda_origem]= [moeda_destino]
    return dic_conversao_disponiveis
