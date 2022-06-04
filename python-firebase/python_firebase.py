import pyrebase
from tkinter import *
import tkinter as tk
import json
from time import sleep

def CadastrarEmpresa():
    def BuscarNomeEmpresa():
        def Concluir():
            janela.destroy()

        nome_empresa = input_name.get()
        json_empresa = {'empresa': nome_empresa}

        json_object = json.dumps(json_empresa, indent = 4) 
        try:
            with open("config/config.json", "w") as arquivo_json: 
                arquivo_json.write(json_object)

            texto_retorno = 'Empresa cadastrada com sucesso'

        except:
            texto_retorno = 'Problema ao cadastrar empresa'

        label_retorno = Label(janela, text=texto_retorno)
        label_retorno.place(x=100,y=100)
        
        botao_concluido = Button(janela, width=20, text='Concluído', command=Concluir)
        botao_concluido.place(x=300,y=100)

    janela = tk.Tk()
    janela.geometry('600x400+100+100')

    input_name = Entry(janela, width=20)
    input_name.place(x=100, y=50)

    botao_cadastrar = Button(janela, width=40, text='Cadastrar', command=BuscarNomeEmpresa)
    botao_cadastrar.place(x=150, y=50)

    janela.mainloop()


with open('config/config.json', encoding='utf-8') as meu_json:
    ler_config = json.load(meu_json)

if ler_config['empresa'] == 0:
    CadastrarEmpresa()

config = {
    "apiKey": "AIzaSyDVyPsRvmfFwH3hASMeqLrpMElyeP48RRw",
    "authDomain": "projete-2022.firebaseapp.com",
    "databaseURL": "https://projete-2022-default-rtdb.firebaseio.com",
    "projectId": "projete-2022",
    "storageBucket": "projete-2022.appspot.com",
    "messagingSenderId": "392429305078",
    "appId": "1:392429305078:web:31e7a9605638bbc20380d7",
    "measurementId": "G-31C7LKYKWP"
}

firebase = pyrebase.initialize_app(config)

base_dados = firebase.database()

with open('config/config.json', encoding='utf-8') as meu_json:
    ler_config = json.load(meu_json)

empresa = ler_config['empresa']

def BuscarFuncionario(empresa):
    nome_funcionario = input('Digite o nome do funcionário: ')
    nome_funcionario_base_dados = empresa+'/funcionarios/'+nome_funcionario
    while True:
        funcionario = base_dados.child(nome_funcionario_base_dados).get()

        try:
            for var in funcionario.each():
                setor = var.val()
                break

        except:
            print('Funcionário não cadastrado')
            epis='Funcionário não cadastrado'
            return epis, nome_funcionario
            break
        
        setor = empresa+'/setores/'+setor
        setor = base_dados.child(setor).get()

        try:
            for var in setor.each():
                epis = var.val()
                return epis, nome_funcionario
                break
        except:
            print('Problema ao encontrar setor')

        break

epis, nome_funcionario = BuscarFuncionario(empresa)

print('Funcionário: ', nome_funcionario)
print("EPI's: ", epis)
