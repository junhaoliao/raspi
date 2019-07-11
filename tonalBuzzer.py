# this program plays "twinkle twinkle little star"thru a tonal buzzer
# for every 7 notes a normal buzzer will ring once

from gpiozero import *
from time import *

tbz = TonalBuzzer(18) # the tonal buzzer is attached to GPIO18
bz = Buzzer(13)  # the normal buzzer is attached to GPIO13

twinkle_twinkle = [
    "C4", "C4", "G4", "G4", "A4", "A4", "G4",
    "F4", "F4", "E4", "E4", "D4", "D4", "C4",

    "G4", "G4", "F4", "F4", "E4", "E4", "D4",
    "G4", "G4", "F4", "F4", "E4", "E4", "D4",

    "C4", "C4", "G4", "G4", "A4", "A4", "G4",
    "F4", "F4", "E4", "E4", "D4", "D4", "C4",
]

def play_song(songName):
    cnt = 0
    for note in songName:
        tbz.play(note)
        sleep(0.15)
        tbz.stop()
        sleep(0.03)
        cnt += 1
        if (cnt == 7):
            bz.on()
            cnt = 0
            sleep(0.15)
            bz.off()


play_song(twinkle_twinkle)
