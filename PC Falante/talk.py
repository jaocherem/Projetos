import pyttsx3

text = 'vai se fuder'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

engine.say(text)
engine.runAndWait()