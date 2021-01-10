from audioop import tomono
import locale
import os
from datetime import datetime
from typing import ContextManager
import webbrowser
import backend
import time
import user
import json

locale.setlocale(locale.LC_ALL, '')
module = backend.Backend()
class Function:
    def __init__(self):
        self.user=user.User()
    def Save(self):
        self.user.Export()
    def UpdateInfo(self,type):
    
        if type in self.user.data.keys():
            if type =="name":
                module.speak("İsmin nedir ?")
                isim = module.hear()
                self.user.data["name"]=isim
            elif type =="surname":
                module.speak("Soyismin nedir ?")
                soyisim = module.hear()
                self.user.data["soyisim"]=soyisim
            elif type=="age":
                module.speak("Kaç yaşındasın ?")
                yas=module.hear()
                self.user.data["age"]=yas
    def Clock(self):
        now = datetime.now()
        clk=(now.strftime("%H:%M:%S"))
        return clk
    
    def Date(self):
        now = datetime.now()
        date= datetime.strftime(now, '%x')
        return date
        
    def search_it(self,search):
        url="https://www.google.com/search?q="+search
        module.speak("İşte senin için bulduklarım: ")
        webbrowser.get().open(url)
        
    
    def GetInfo(self,type):
        if type in self.user.data.keys():
            return self.user.data[type]
        else:
            print("Bilgi bulunamadı.")
            
