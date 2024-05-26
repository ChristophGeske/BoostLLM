# Thats a simple version that works with only 4 lines of code and is super fast, but the quality is not that great
import pyttsx3
engine = pyttsx3.init()
engine.say("Text to speech is working and it is quick! It is so simple just 4 lines of code are enough. The question is how the quality is compared to implementations that take more time.")
engine.runAndWait()