# Thats a simple version that works with only a few lines of code, no fancy imports and it is super fast, but the quality is not that great
import time

from RealtimeTTS import TextToAudioStream, SystemEngine

engine = SystemEngine() # replace with your TTS engine
stream = TextToAudioStream(engine)
stream.feed("Text to speech is working and it is quick! It is so simple just 4 lines of code are enough. The question is how the quality is compared to implementations that take more time.")
stream.play_async()

while stream.is_playing():
    time.sleep(0.1)