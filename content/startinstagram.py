from urllib.request import urlopen
from functions import ultraDebug, socialNetwork, read_json
from datetime import datetime
import pyautogui
import webbrowser
import time
import json


date = datetime.now()

# alocando o conteudo na memoria
data = read_json()

# busca a url do instagram
url = data['config']['network']['instagram']['url']

# aguardar o time de 3 segundos para o próximo step
time.sleep(3.0)

# gerando log
ultraDebug(date, 'Navegando no Instagram agora')

#navegando no instagram
socialNetwork(url)

# mover o ponteiro do mouse para posicição desejada
pyautogui.moveTo(850,150)

html = urlopen(url)
# print(html.read())