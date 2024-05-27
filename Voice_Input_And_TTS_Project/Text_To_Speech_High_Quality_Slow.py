# TODO Do a "pip install coqui-tts" in the command line window to install the library
# TODO You might also need to do "pip install --upgrade pip setuptools wheel" and install the Microsoft C++ Build Tools on windows
# TODO When you run the code you then need to agree to the terms of coqui.ai which takes some time.
# TODO You might need to install the CUDA Toolkit by running pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
import io
import time

import torch
from TTS.api import TTS

from pydub import AudioSegment
from pydub.playback import play

# Debugging: Check if CUDA is available and print the GPU name if available
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")
if cuda_available:
    print(f"GPU Acceleration Enabled: Running on {torch.cuda.get_device_name(torch.cuda.current_device())}")
else:
    print("GPU Acceleration Not Enabled: Running on CPU")

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# ----- Different TTS implementations and their corresponding times -----

# -- Version 1 || TTS implementation with custom voice provided by the speaker_wav audio file --
'''
# Initialize TTS with a pre-trained model that expects a speaker_wav audio file
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.to(device)

start_time = time.time()
tts.tts_to_file(text="Text to speech is working and it is quick! It is so simple just 4 lines of code are enough. The question is how the quality is compared to implementations that take more time.",
                file_path="output1.wav",
                # TODO Change the path to your own high quality voice example
                speaker_wav="C:/Users/chris/OneDrive/Dokumente/GitHub/LLMsBooster/Voice_Input_And_TTS_Project/voices/female.wav",
                language="en")
end_time = time.time()
# Print time taken for generation
print(f"Time taken for TTS generation + retraining the voice: {end_time - start_time} seconds")

# Load and play the audio file
audio = AudioSegment.from_wav("output1.wav")
play(audio)
'''

# -- Version 2 || TTS implementation with a fixed high quality voice running much faster. --

start_time = time.time()
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
tts.to(device)
end_time = time.time()
print(f"Time taken to load model: {end_time - start_time} seconds")

# Generate speech and save to file
start_time = time.time()
tts.tts_to_file(
    text="Text to speech is working and it is quick! It is so simple just a few lines of code are enough. The question is how the quality is compared to implementations that take more time.",
    file_path="output2.wav"
)
end_time = time.time()
print(f"Time taken for TTS generation with a pretrained voice: {end_time - start_time} seconds")

audio = AudioSegment.from_wav("output2.wav")
play(audio)

# -- Version 3 || Very short word TTS generation for speed comparison

start_time = time.time()
tts.tts_to_file(
    text="Hello World!",
    file_path="output3.wav"
)
end_time = time.time()
print(f"Time taken for Short Word TTS generation: {end_time - start_time} seconds")

audio = AudioSegment.from_wav("output3.wav")
play(audio)