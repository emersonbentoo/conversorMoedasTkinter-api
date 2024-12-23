import customtkinter
customtkinter.set_appearance_mode("dark-blue")
janela = customtkinter.CTk()
janela.geometry("500x500")
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas",font=("",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela,text="Selecione moeda destino")

moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD","BRL","EURO","BTC"])
moeda_destino = customtkinter.CTkOptionMenu(janela,values=["USD","BRL","EURO","BTC"])

def converter_moedas():
    print("Converter Moedas")                                            
botao_converter= customtkinter.CTkButton(janela,text="Converter",command="converter_moedas")                                            

detalhe=customtkinter.CTkScrollableFrame(janela)
moedas_disponiveis = ["USD: Dolar americano","BRL: Real brasileiro","BTC: Bitcoin"]
for moedas in moedas_disponiveis:
    texto_moeda= customtkinter.CTkLabel(detalhe,text=moedas)
    texto_moeda.pack()




titulo.pack(padx=10,pady = 10)
texto_moeda_origem.pack(padx=1,pady=10)
moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10)
moeda_destino.pack(padx=10,pady=10)
botao_converter.pack()
detalhe.pack(padx=10,pady=10)
janela.mainloop()