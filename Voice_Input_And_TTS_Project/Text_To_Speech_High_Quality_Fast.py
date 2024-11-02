# time needed only 9 seconds even for very long texts.

import time
import torch
from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import threading
import re
import queue

# Function to split text into sentences
def split_text_into_sentences(text):
    # Split text using regular expression to match sentence endings
    sentences = re.split(r'(?<=[.!?])', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# Function to play audio
def play_audio(file_path):
    audio = AudioSegment.from_wav(file_path)
    play(audio)

# Function to generate TTS for a chunk of text and add to the queue
def generate_tts(chunk, index, tts, device, q):
    file_path = f"output_chunk_{index}.wav"
    tts.tts_to_file(
        text=chunk,
        file_path=file_path
    )
    q.put(file_path)

# Debugging: Check if CUDA is available and print the GPU name if available
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")
if cuda_available:
    print(f"GPU Acceleration Enabled: Running on {torch.cuda.get_device_name(torch.cuda.current_device())}")
else:
    print("GPU Acceleration Not Enabled: Running on CPU")

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize TTS
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
tts.to(device)

# Long text to be synthesized
long_text ='The AI winter is often seen as a reaction to the overly optimistic predictions and promises made by AI researchers and the media.',
long_text = ' '.join(long_text)
# Split the long text into sentences
sentences = split_text_into_sentences(long_text)

# Queue to hold generated audio file paths
audio_queue = queue.Queue()

# Function to process the audio queue
def process_audio_queue(q):
    while True:
        file_path = q.get()
        if file_path is None:
            break
        play_audio(file_path)
        q.task_done()

# Start the audio queue processing thread
audio_thread = threading.Thread(target=process_audio_queue, args=(audio_queue,))
audio_thread.start()

# Generate TTS and add to the queue in the main thread
for i, sentence in enumerate(sentences):
    generate_tts(sentence, i, tts, device, audio_queue)

# Signal the audio thread to stop after all files are processed
audio_queue.put(None)

# Wait for the audio queue to be fully processed
audio_queue.join()

# Wait for the audio thread to complete
audio_thread.join()

print("All TTS and audio playback threads have completed.")

