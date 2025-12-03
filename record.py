import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="input.wav", duration=4, fs=44100, device=10):
    print("🎙️ Recording... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=device)
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Saved: {filename}")
