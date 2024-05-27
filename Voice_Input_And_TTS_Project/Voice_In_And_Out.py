import sounddevice as sd
import whisper
import torch
from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import re
import queue
import threading

# Load the Whisper model
model = whisper.load_model("base")

# Record audio for 7 seconds
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
transcription = result["text"]
print("Transcription:", transcription)

# Function to split text into sentences
def split_text_into_sentences(text):
    sentences = re.split(r'(?<=[.!?])', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# Function to play audio
def play_audio(file_path):
    audio = AudioSegment.from_wav(file_path)
    play(audio)

# Function to generate TTS for a chunk of text and add to the queue
def generate_tts(chunk, index, tts, device, q):
    file_path = f"output_chunk_{index}.wav"
    tts.tts_to_file(text=chunk, file_path=file_path)
    q.put(file_path)

# Check if CUDA is available
cuda_available = torch.cuda.is_available()

# Get device
device = "cuda" if cuda_available else "cpu"

# Initialize TTS
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
tts.to(device)

# Split the transcription into sentences
sentences = split_text_into_sentences(transcription)

# Queue to hold generated audio file paths
audio_queue = queue.Queue()

# Function to process the audio queue
def process_audio_queue(q):
    while True:
        file_path = q.get()
        if file_path == "STOP":
            q.task_done()  # Mark "STOP" task as done before breaking
            break
        play_audio(file_path)
        q.task_done()  # Mark the current task as done

# Start the audio queue processing thread
audio_thread = threading.Thread(target=process_audio_queue, args=(audio_queue,))
audio_thread.start()

# Generate TTS and add to the queue in the main thread
for i, sentence in enumerate(sentences):
    generate_tts(sentence, i, tts, device, audio_queue)

# Signal the audio thread to stop after all files are processed
audio_queue.put("STOP")

# Wait for the audio queue to be fully processed
audio_queue.join()

# Wait for the audio thread to complete
audio_thread.join()

print("All TTS and audio playback threads have completed.")
