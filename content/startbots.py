from os.path import dirname, realpath, isfile
from json import dump
import tkinter as tk
from functions import ultraDebug
import sys
import json


class JsonStartBots:
    def __init__(self):
        self.path = dirname(realpath(__file__))

    def create_json(self, file):
        data = {
                "config": {
                            "network": {
                                "default": {
                                    "network-social": "Default",
                                    "url": "https://www.google.com/",
                                    "mensagem": "Default setting has been set."
                                },
                                "facebook": {
                                    "network-social": "Facebook.Inc",
                                    "url": "https://www.facebook.com/",
                                    "mensagem": "Facebook setting has been set."
                                },
                                "instagram": {
                                    "network-social": "Instagram.Inc",
                                    "url": "https://www.instagram.com/",
                                    "mensagem": "Instagram setting has been set."
                                },
                                "linkedin": {
                                    "network-social": "LinkedIn.Inc",
                                    "url": "https://br.linkedin.com/",
                                    "mensagem": "Linkedin setting has been set."
                                },
                                "telegram": {
                                    "network-social": "Telegram.Inc",
                                    "url": "https://web.telegram.org/#/login",
                                    "mensagem": "Telegram setting has been set."
                                },
                                "twitter": {
                                    "network-social": "Twitter.Inc",
                                    "url": "https://twitter.com/explore/",
                                    "mensagem": "Twitter setting has been set."
                                },
                                "whatsapp": {
                                    "network-social": "Whatsapp.Inc",
                                    "url": "https://web.whatsapp.com/",
                                    "mensagem": "WhatsApp setting has been set."
                                }
                            }
                        },

            "credential": {
                "network": {
                    "facebook": {
                        "username": "ageu87@gmail.com",
                        "password": "215487"
                    }
                }
                        }
                }
        path_data_json =self.path + file
        if not isfile(path_data_json):
            with open(path_data_json, 'w', encoding="UTF-8") as f:
                dump(data, f)

            return True

        else:
            return False

if __name__ == '__main__':
    jmanager = JsonStartBots()
    jmanager.create_json('/config/config.json')
    ultraDebug('Arquivo de configuração criado com sucesso')


# Classe para gerar a tela de logins

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] ="Hello World\n(click me)"
        self.hi_there["command"] =self.say_hi
        self.hi_there.pack(side="top")

        self.quit =tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")
    def say_hi(self):
        print("hi there, everyone")
root =tk.Tk()
app = Application(master=root)
app.mainloop()