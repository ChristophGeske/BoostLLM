# TODO Do a "pip install coqui-tts" in the command line window to install the library
# You might also need to do "pip install --upgrade pip setuptools wheel" and install the Microsoft C++ Build Tools on windows
# When you run the code you then need to agree to the terms of coqui.ai which takes some time.

import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize TTS with a pre-trained model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=device == "cuda")

# generate speech by cloning a voice using default settings
# This took around 17 seconds to generate a hello on my laptop with Nvidia GPU 3080 laptop without other GPU demanding software running
tts.tts_to_file(text="Hello",
                file_path="output.wav",
                speaker_wav="C:/Users/chris/OneDrive/Dokumente/GitHub/LLMsBooster/Voice_Input_And_TTS_Project/voices/female.wav",
                language="en")

