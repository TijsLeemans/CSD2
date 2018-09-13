import simpleaudio as sa
import wave

wave_read = wave.open("Audiofiles\PhantomHigh.wav")
audio_data = wave_read.readframes(wave_read.getnframes())
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()

wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
play_obj = wave_obj.play()
play_obj.wait_done()
