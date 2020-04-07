from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import csv
from functions import ultraDebug, socialNetwork, read_json
from datetime import datetime
import pyautogui
import webbrowser
import time
import json



#Facebook API
token ='EAADJdtrk1voBAO8xPbY8noy9n9ymS0HaS6cZCKQ4Du9bEhsjveAxk0TvZCPIqjMILnFVcWMysD8qgZBY5YG4iCxf6SZCQpne4cZBUEuZCM5zNdsH7HlcaRxaSVc5AU8o5cyzguZAOAgj8XlOv7MCY8JEeLQZA2gzs0cOIjyyULcxYEsruL4fJrPalSZBLUDL3IUa4WkyXf5UP7jFiLXXZClVm4DHg9cZB6cBZCZCWulpQKzogrQZDZD'
me = 'https://graph.facebook.com/v6.0/me?access_token=

date = datetime.now()

# alocando o conteudo na memória
data = read_json()

# busca a url do facebook
url = data['config']['network']['facebook']['url']

# aguardar o time de 3 segundos para o próximo step
time.sleep(3.0)

# gerando log
ultraDebug(date,'Navegando no facebook agora')

#abre o browser com a url encontrada
socialNetwork(url)

# start time de 1 segundo para pegar o codigo do site para analisar
time.sleep(1.0)

# aloca o codigo do site na memoria
html = urlopen(url)

#nome = []

soup = BeautifulSoup(html, 'lxml')

# titulo da página do facebook
title = soup.title.string

#mostrar as divs da pagina
div =  soup.div['class']

#df = pd.DataFrame({'nome':nome})

# mostra no console o codigo do site
print(div)