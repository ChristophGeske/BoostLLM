# sounddevice is used for recording audio it stores the audio in a numpy array.
# In terminal do pip install sounddevice to install the package
import sounddevice as sd
import numpy as np
# whisper for speech recognition and transcription.
import whisper
import threading
import queue
import time

# Load the Automatic Speech Recognition (ASR) Whisper model used to transcribe audio data into text.
model = whisper.load_model("base")

# Define a queue to hold audio data chunks. Used to pass audio data from the recording thread to the transcription thread.
audio_queue = queue.Queue()

# For detection of silence in the audio stream define a function to calculate RMS (Root Mean Square) of the audio data.
def calculate_rms(audio_data):
    return np.sqrt(np.mean(audio_data**2))

# Define the chunk size of audio data that is passed in one block to the Whisper model.
# Performs better with longer chunk sizes because the model has more context to transcribe the speech accurately.
# 16000 samples = 1 second of audio therefore 112000 samples = 7 seconds before the transcription is generated.
chunk_Size = 112000

# Define a function to process and transcribe the audio data. This function runs in a separate thread
# and continuously reads audio data from the queue, transcribes it into text using the Whisper model,
# and prints the transcription. It also detects silence in the audio stream and stops the transcription
# after 2 seconds of silence.
def transcribe():
    buffer = np.zeros(0, dtype=np.float32)
    silence_counter = 0
    while True:
        audio_data = audio_queue.get()
        if audio_data is None:
            break
        buffer = np.concatenate((buffer, audio_data))
        # Chunk size: The Whisper model might perform better with longer audio clips.
        # If the chunks are too short, the model might not have enough context to accurately transcribe the speech.
        # Increasing the blocksize to record longer chunks of audio.
        # Longer chunks of audio can improve the accuracy of the transcription but may introduce a delay in the transcription.
        if len(buffer) >= chunk_Size:  # Process in chunks of 1 second
            # If the RMS of the audio data is below a certain threshold, consider it to be silence
            if calculate_rms(buffer[:chunk_Size]) >= 0.01:  # Only transcribe if there's sound
                result = model.transcribe(buffer[:chunk_Size])
                print("Transcription:", result["text"], flush=True)
            buffer = buffer[chunk_Size:]  # Keep remaining audio data


# Start the transcription thread which runs the transcribe() function.
transcription_thread = threading.Thread(target=transcribe)
transcription_thread.start()

# Define a callback function to record the audio chunks. Whenever there's new audio data available it add it to the queue.
def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    # Add the incoming data to the queue
    audio_queue.put(indata[:, 0].copy())

# Start the stream. Audio data is recorded in 0.1-second chunks and passed to the callback function.
try:
    with sd.InputStream(callback=callback, channels=1, samplerate=16000, dtype=np.float32, blocksize=chunk_Size):  # Record in 0.1-second chunks
        print("Recording and transcribing. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Check the audio every second
# Stop the recording and transcription when Ctrl+C is pressed or 2 second silence detected.
except KeyboardInterrupt:
    print("Stopping...")
finally:
    audio_queue.put(None)  # Signal the transcription thread to exit
    transcription_thread.join()

