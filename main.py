import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(rate=RATE,
                channels=CHANNELS,
                format=FORMAT,
                input=True,output=False)

print("Recording...")
frames = []
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Recording finished.")

stream.stop_stream()
stream.close()

output_file_name = "recorded_audio.wav"
wf = wave.open(output_file_name,"wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("Recording saved as", output_file_name)

p.terminate()

