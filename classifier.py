import librosa
from os import path
from pydub import AudioSegment
import shutil
import os
from pathlib import Path

entries = Path('/Users/playment/Parth /Codes/SoundMixer/songs')
for entry in entries.iterdir():
    # print(entry.name)
    a = entry.name
    src = ("/Users/playment/Parth /Codes/SoundMixer/songs/" + a)
    dst = ("/Users/playment/Parth /Codes/SoundMixer/songs/" + a  + ".wav")


    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

    filename = ("/Users/playment/Parth /Codes/SoundMixer/songs/" + a + ".wav")

    y, sr = librosa.load(filename)

    tempo1, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print("Tempo: {:.2f}".format(tempo1))

    if tempo1 > 50 and tempo1 < 70 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class1")
    elif tempo1 > 70 and tempo1 < 80 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class2")
    elif tempo1 > 80 and tempo1 < 90 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class3")
    elif tempo1 > 90 and tempo1 < 100 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class4")
    elif tempo1 > 100 and tempo1 < 110 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class5")
    elif tempo1 > 110 and tempo1 < 120 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class6")
    elif tempo1 > 120 and tempo1 < 130 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class7")
    elif tempo1 > 130 and tempo1 < 140 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class8")
    elif tempo1 > 140 and tempo1 < 150 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class9")
    elif tempo1 > 150 and tempo1 < 160 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class10")
    elif tempo1 > 160 and tempo1 < 170 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class11")
    elif tempo1 > 170 and tempo1 < 180 :
        shutil.move(filename, "/Users/playment/Parth /Codes/SoundMixer/class12")
    else:
        print ("looooooooner")
