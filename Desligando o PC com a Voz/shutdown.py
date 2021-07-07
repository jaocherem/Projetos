import os
import pyttsx3
import speech_recognition as sr
import time

"""
Criação da classe
"""
class cum:

    """
    Método para reconhecer a voz
    """
    def commands(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Ouvindo')
            audio = r.listen(source)

            """
            Ajustando o programa para entender português e manusear erro
            """
            try:
                statement = r.recognize_google(audio, language='pt-BR')

            except Exception as e:
                print(e)
                print("Repita")
                return "None"
        return statement

    """
    Método da fala
    """
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')

        # Ajustando o tipo de voz
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    """
    Método para desligar
    """
    def shutdown(self):
        take = self.commands()
        choices = take

        """
        Se a palavra 'desliga' for identificada na fala o computador irá desligar
        """
        if "desliga" in choices:
            self.speak("Sim senhor")
            os.system("shutdown /s /t 30")

"""
Parte que vai iniciar ao rodar o programa
"""
if __name__ == '__main__':
    poop = cum()
    poop.shutdown()