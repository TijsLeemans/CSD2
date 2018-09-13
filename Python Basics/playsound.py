import simpleaudio as sa
import wave
import time
n = int(input("zeg het maar, hoe vaak wil je hem hebben? "))

def player(n):
    if n == 0:
        print("okiii klaar... daaaaag!")
        time.sleep(1)
        return
    else:
        print(n)
        wave_read = wave.open("Audiofiles\snare-1.wav")
        audio_data = wave_read.readframes(wave_read.getnframes())
        num_channels = wave_read.getnchannels()
        bytes_per_sample = wave_read.getsampwidth()
        sample_rate = wave_read.getframerate()

        wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        return (player(n-1))
player(n)
