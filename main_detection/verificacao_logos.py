from time import sleep
import cv2
import json
from cv2 import COLOR_BGR2GRAY
import pyrebase
from datetime import *

# -------------------- BUSCA DO FUNCIONÁRIO NO FIREBASE --------------------
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


def CriarListaEPIS(epis):
    lista_epis = []

    if epis['capacete'] == True:
        lista_epis.append('capacete')
    if epis['luvas'] == True:
        lista_epis.append('luvas')
    if epis['colete'] == True:
        lista_epis.append('colete')
    if epis['oculos'] == True:
        lista_epis.append('oculos')
    if epis['pa'] == True:
        lista_epis.append('pa')
    if epis['botas'] == True:
        lista_epis.append('botas')

    return lista_epis

epis, nome_funcionario = BuscarFuncionario(empresa)

lista_epis = CriarListaEPIS(epis)
print(lista_epis)

capacete = epis['capacete']
luvas = epis['luvas']
colete = epis['colete']
oculos = epis['oculos']
pa = epis['pa']
botas = epis['botas']

epis_detectadas = 0
capacete_detectado = False
colete_detectado = False 
botas_detectado = False
oculos_detectado = False
luvas_detectado = False
pa_detectado = False
funcionario_verificado = False

numero_epis = len(lista_epis)

cascade_logo_capacete = cv2.CascadeClassifier('cascades/cascade_instagram.xml')
cascade_logo_botas = cv2.CascadeClassifier('cascades/cascade_logo.xml')
cascade_logo_colete = cv2.CascadeClassifier('cascades/cascade.xml')
cascade_logo_luvas = cv2.CascadeClassifier('cascades/cascade.xml')
cascade_logo_pa = cv2.CascadeClassifier('cascades/cascade.xml')
cascade_logo_oculos = cv2.CascadeClassifier('cascades/cascade.xml')

camera = cv2.VideoCapture(0)

moment = datetime.now()
segundos1 = moment.second
print(segundos1)
sleep(0.5)
segundos2 = 0

while segundos1 != segundos2:
    moment2 = datetime.now()
    segundos2 = moment2.second + 1
    print("---------------------------", segundos2, "---------------------------")
    _, video = camera.read()

    video_cinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    if capacete == True:
        deteccao_capacete = cascade_logo_capacete.detectMultiScale(video_cinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
        print(deteccao_capacete)
        if (deteccao_capacete != ()):
            print('capacete detectado')
            capacete_detectado = True

    if botas == True:
        deteccao_botas = cascade_logo_botas.detectMultiScale(video_cinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
        print(deteccao_botas)
        if (deteccao_botas != ()):
            print('botas detectado')
            botas_detectado = True

    if colete == True:
        deteccao_colete = cascade_logo_colete.detectMultiScale(video_cinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
        print(deteccao_colete)
        if (deteccao_colete != ()):
            print('colete detectado')
            colete_detectado = True

    if luvas == True:
        deteccao_luvas = cascade_logo_luvas.detectMultiScale(video_cinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
        print(deteccao_luvas)
        if (deteccao_luvas != ()):
            print('luvas detectado')
            luvas_detectado = True
    
    if pa == True:
        deteccao_pa = cascade_logo_pa.detectMultiScale(video_cinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
        print(deteccao_pa)
        if (deteccao_pa != ()):
            print('pa detectado')
            pa_detectado = True

    if oculos == True:
        deteccao_oculos = cascade_logo_oculos.detectMultiScale(video_cinza, scaleFactor=1.33, minNeighbors=10, minSize=(40,40))
        print(deteccao_oculos)
        if (deteccao_oculos != ()):
            print('oculos detectado')
            oculos_detectado = True

    for (x,y,l,a) in deteccao_capacete:
        cv2.rectangle(video_cinza, (x, y), (x + l, y + a), (0,255,0), 2)

    for (x,y,l,a) in deteccao_botas:
        cv2.rectangle(video_cinza, (x, y), (x + l, y + a), (0,255,0), 2)
    
    for (x,y,l,a) in deteccao_colete:
        cv2.rectangle(video_cinza, (x, y), (x + l, y + a), (0,255,0), 2)

    cv2.imshow('Video', video_cinza)

    for i in lista_epis:
        print('numero epis: ', numero_epis)
        print('epis detectadas: ', epis_detectadas)
        print(i)

        if i == 'capacete':
            if capacete_detectado == True:
                epis_detectadas = epis_detectadas + 1
                lista_epis.remove('capacete')

        if i == 'botas':
            if botas_detectado == True:
                epis_detectadas = epis_detectadas + 1
                lista_epis.remove('botas')

        if i == 'colete':
            if colete_detectado == True:
                epis_detectadas = epis_detectadas + 1
                lista_epis.remove('colete')

        if i == 'luvas':
            if luvas_detectado == True:
                epis_detectadas = epis_detectadas + 1
                lista_epis.remove('luvas')

        if i == 'pa':
            if pa_detectado == True:
                epis_detectadas = epis_detectadas + 1
                lista_epis.remove('pa')

        if i == 'oculos':
            if oculos_detectado == True:
                epis_detectadas = epis_detectadas + 1
                lista_epis.remove('oculos')

        if epis_detectadas == numero_epis:
            print("epis_detectadas para finalizar: ", epis_detectadas)
            print("Funcionário usando todas as EPI's")
            funcionario_verificado = True
            break

    if cv2.waitKey(1) == ord('q'):
        break

    if funcionario_verificado == True:
        break

if funcionario_verificado == False:
    print('Funcionário não está usando todas as epis')
camera.release()
cv2.destroyAllWindows()