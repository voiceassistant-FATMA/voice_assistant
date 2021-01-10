import os
import json
import function
import backend
class Commands():
    def __init__(self,function,module):
        self.function = function
        self.module = module
        with open("./Data/commands.json","r",encoding='utf8') as file:
            self.commands=json.load(file)

    def Run(self,data):
        for key in self.commands.keys():
            for command in self.commands[key]:
                if data in self.commands[key][command]:
                    return self.Execute(command,key)
        self.module.speak("Bir şeyler ters gitti.")
        return 1
        
    def Execute(self,command,commandType):
        if(commandType=="update"):
            if(command=="isimguncelle"):
                self.function.UpdateInfo("name")
                self.module.speak("İsmini {} olarak güncelledim".format(self.function.GetInfo("name")))
            elif(command=="yasguncelle"):
                self.function.UpdateInfo("age")
        elif(commandType=="getInfo"):
            if(command=="meslekgetir"):
                self.function.GetInfo("job")
        elif(commandType=="asistanInfo"):
            if(command=="kendinitanit"):
                self.module.speak("Merhabalar benim adım Fatma. Ben bir sesli asistanım")
            elif(command=="isimsoru"):
                self.module.speak("Benim adım Fatma")
        elif(commandType=="timeFunctions"):
            if(command=="saatSoru"):
                self.module.speak("Şu an saat "+self.function.Clock())
            elif(command=="tarihSoru"):
                self.module.speak("Bugün: "+self.function.Date())
        elif(commandType=="close"):
            if(command=="kapat"):
                self.module.speak("Görüşmek üzere {}".format(self.function.GetInfo("name")))
                return 0
        else:
            self.module.speak("Bir şeyler ters gitti.")
        return 1
    
