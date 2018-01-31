# DJ TB 4 LIF
# John Heitz
# 1/16/2018
# DJ RASI iz in da house
import RPi.GPIO as GPIO
import time
import random
import os
path_ML= "/usr/share/scratch/Media/Sounds/Music Loops/"
path_vocals="/usr/share/scratch/Media/Sounds/Vocals/"
path_effects="/usr/share/scratch/Media/Sounds/Effects/"
def get_MP3_sounds(sound_path):
     sound_filesound_files =os.listdir(sound_path)
     sound_filesound_files =[sound_file for sound_file in sound_filesound_files if sound_file.endswith('.mp3')]
     return sound_filesound_files
def play_random_sound(sound_path,sound_filesound_files):
    random_sound_index=random.randint(0, len(sound_filesound_files)-1)
    os.system("omxplayer -o local '" + sound_path + "/" +sound_filesound_files[random_sound_index] + "' &")
ML_button=6
vocals_button=19



GPIO.setmode(GPIO.BCM)


GPIO.setup(ML_button, GPIO.IN)
GPIO.setup(vocals_button, GPIO.IN)

sounds_ML= get_MP3_sounds(path_ML)
sounds_vocals= get_MP3_sounds(path_vocals)
sounds_effects= get_MP3_sounds(path_effects)
os.system("clear")
print("YO YO YO! DJ RASI IZ IN DA HIZZY!PRESS B1 FO MUSIC LOOP! PRESS B2 FO TALKIN! CONTROL C = BREAK IT DOWN!")
while 1<2:
    if GPIO.input(ML_button):
        print("TECHNO TIMEIMEIMEIMEIME!")
        play_random_sound(path_ML, sounds_ML)
        time.sleep(.1)
    if GPIO.input(vocals_button):
        print("TIME FO DA SINGIN FOOL!")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(.1)
    if GPIO.input(ML_button) and GPIO.input(vocals_button): 
        play_random_sound(path_effects, sounds_effects)
        print("Time for easter.")
        time.sleep(.1)
    time.sleep(.1)
