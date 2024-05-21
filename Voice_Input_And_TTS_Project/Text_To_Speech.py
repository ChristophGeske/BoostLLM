# All you need for TTS to work are these 4 lines
import pyttsx3
engine = pyttsx3.init()
engine.say("Text to speech is working! It is so simple just 4 lines of code.")
engine.runAndWait()