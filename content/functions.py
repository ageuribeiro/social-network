from datetime import datetime
import webbrowser
import pyautogui
import time
import json
import os




# função para gerar log
def ultraDebug(data, msg):
    data_atual = data.strftime('%d/%m/%Y %H:%M:%S:%M')

    print(data_atual, '-' ,msg)
    check_filelog = os.path.isfile('log.txt')

    if( check_filelog == False):
        filelog = open('log.txt', 'w', encoding='UTF-8')

    filelog = open('log.txt', 'r', encoding='UTF-8')
    content = filelog.readlines()
    content.append('Date: '+ data_atual +
                ' - Action: '+msg+ '\n')
    filelog = open('log.txt', 'w', encoding='UTF-8')
    filelog.writelines(content)
    filelog.close()



# função para ler o arquivo json
def read_json():
    with open('config/config.json', 'r', encoding="UTF-8") as f:
        return json.load(f)


def socialNetwork(url):
    #abre o browser com a url encontrada
    webbrowser.open_new(url)

    # pega a largura e a altura da monitor
    monitor = screenWidth, screenHeight = pyautogui.size()

    #pega a posição do mouse
    mouse = currentMouseX, currentMouseY = pyautogui.position()

    # aguardar o time de 3 segundos para o próximo step
    time.sleep(3.0)