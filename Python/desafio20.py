from pygame import mixer
from time import sleep

mixer.init()
mixer.music.load("arcane.mp3")
mixer.music.play()

sleep(180)