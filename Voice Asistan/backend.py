from gtts import gTTS
import PyQt5.QtCore as coremodule
import PyQt5.QtMultimedia as multimedia
import speech_recognition as sr

import sys
class Backend:
    mic=sr.Microphone()
    r=sr.Recognizer()
    
    def __init__(self):
        self.app = coremodule.QCoreApplication(sys.argv)
    
            
    def hear(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            #print("Arka plan gürültüsü:" + str(r.energy_threshold))
            print("->Fatma Dinliyor...")
            try:
                ses = self.r.listen(source,timeout=5,phrase_time_limit=5)
                yazi = self.r.recognize_google(ses, language="tr-tr")
                return yazi

            except sr.WaitTimeoutError:
                print("Dinleme zaman aşımına uğradı")

            except sr.UnknownValueError:
                print("Ne dediğini anlayamadım")

            except sr.RequestError:
                print("İnternete bağlanamıyorum")
    def playSound(self, audioPath):
        url = coremodule.QUrl.fromLocalFile(audioPath)
        content = multimedia.QMediaContent(url)
        player = multimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(self.app.quit)
        self.app.exec()

    def speak(self, audioString):
        tts = gTTS(text=audioString, lang='tr')
        print("Fatma:"+audioString)
        tts.save("audio.mp3")
        # os.system("audio.mp3")
        self.playSound("audio.mp3")

    def recordAudio(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:#mikrofon algılayamadığı için hata veriyor ama merhaba dedi duymadınız
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio, language='tr-tr')
            data = data.lower()
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Ne dediğini anlamadım")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data