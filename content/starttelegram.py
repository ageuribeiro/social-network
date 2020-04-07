from urllib.request import urlopen
import json

def read_json():
    with open('config/config.json', 'r', encoding="UTF-8") as f:
        return json.load(f)

data = read_json()
url = data['config']['network']['telegram']['url']
html = urlopen(url)
# print(html.read())