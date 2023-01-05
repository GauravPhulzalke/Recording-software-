import sounddevice
from scipy.io.wavfile import write
fs=44100
seconds=10
print("recording...")
record=sounddevice.rec(int(fs*seconds), samplerate=fs, channels=2)
sounddevice.wait()
write(r"C:\Users\91837\OneDrive\Desktop\Raanjhanaa.wav", fs, record)