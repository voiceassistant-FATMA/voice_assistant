#Kütüphanelerimizi Tanımlıyoruz.
from audioop import tomono
import locale
import os
import time
import backend
import sys
import signal
import function
import speech_recognition as sr
import user
import commands
locale.setlocale(locale.LC_ALL, '')

#Burada ise fonksiyona verilen metin içerisinde yakalanan metinler komut mu diye kontrol ediliyor 
def asistan(data):
    if data=="&&":
        module.sleep()
        return 1
    else:
        return commands.Run(data)
        
onoffswitch = 1
if onoffswitch:
    function = function.Function()
    module = backend.Backend()
    commands =commands.Commands(function,module)
    module.speak("Merhaba {} Hoşgeldin".format(function.GetInfo("name")))
    i=1
    while i:
        i = asistan(module.hear())
    function.Save()