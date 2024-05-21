import sounddevice as sd
import numpy as np
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Record audio for 7 seconds. TODO: Speak for 7 sec and see if it recorded the audio and prints the transcript.
duration = 7  # seconds
samplerate = 16000
print("Recording...")
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
sd.wait()
print("Recording finished.")

# Reshape audio to match Whisper input requirements
audio = audio.flatten()

# Transcribe the audio
result = model.transcribe(audio)
print("Transcription:", result["text"])




