import customtkinter 
from buscar_moedas import nomes_moedas, conversao_disponiveis
from requisicao import buscar_cotacao

customtkinter.set_appearance_mode("dark-blue")
janela = customtkinter.CTk()
janela.geometry("500x500")
dic_conversao_disponiveis=conversao_disponiveis()


titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas",font=("",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela,text="Selecione moeda destino")

def carregar_moedas_destino(moedas_selecionada):
    lista_moedas_destino= dic_conversao_disponiveis[moedas_selecionada]
    moeda_destino.configure(values = lista_moedas_destino)
    moeda_destino.set(lista_moedas_destino[0])
    

moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversao_disponiveis.keys()), command= carregar_moedas_destino)
moeda_destino = customtkinter.CTkOptionMenu(janela,values=["Selecione moedas de origem"])

def converter_moedas():
    origem= moeda_origem.get()
    destino = moeda_destino.get()
    if origem and destino:
        cotacao = buscar_cotacao(origem,destino)
        try:
            cotacao_float = float(cotacao)
            valor_cotacao.configure(text=f"1 {origem} = {cotacao_float:.2f} {destino}")
        except ValueError:
            valor_cotacao.configure(text="Erro: Cotação inválida.")

botao_converter= customtkinter.CTkButton(janela,text="Converter",command=converter_moedas)                                            

detalhe=customtkinter.CTkScrollableFrame(janela)


valor_cotacao =customtkinter.CTkLabel(janela,text="")

moedas_disponiveis = nomes_moedas()

for cod_moedas in moedas_disponiveis:
    nome_da_moeda = moedas_disponiveis[cod_moedas]
    texto_moeda= customtkinter.CTkLabel(detalhe,text=f"{cod_moedas}:{nome_da_moeda}")
    texto_moeda.pack()




titulo.pack(padx=10,pady = 10)
texto_moeda_origem.pack(padx=1,pady=10)
moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10)
moeda_destino.pack(padx=10,pady=10)
botao_converter.pack()
valor_cotacao.pack(padx=10,pady=10)
detalhe.pack(padx=10,pady=10)


janela.mainloop()