import simpleaudio as sa
import time

#input nootwaardes, aantal maten en bpm.
nootValue1 = float(input("Nootlengte 1? "))
nootValue2 = float(input("Nootlengte 2? "))
nootValue3 = float(input("Nootlengte 3? "))
nootValue4 = float(input("Nootlengte 4? "))
maatValue = int(input("Aantal maten? "))
BPM = float(input("met een tempo van?"))

#import sample en naamgeving
def playSnare():
    wave_obj = sa.WaveObject.from_wave_file("Audiofiles/snare-1.wav")
    play_obj = wave_obj.play()

#nootwaardes tot lijst
values = [nootValue1, nootValue2, nootValue3, nootValue4,]
numValues = len(values)

#aanmaken van hoofdfuctie
def player(maatValue):
    if maatValue == 0:                      #controle aantal maten
        print("okiii klaar... daaaaag!")
        time.sleep(1)
        return
    else:                                   #afspelen 1 maat
        for value in values:
            print(value)
            playSnare()
            time.sleep((60/BPM)*value)
                                            #forloop exit en herstart maat controle
        return (player(maatValue-1))

#oproepen fuctie bij het aanroepen van dit programma.
player(maatValue)
