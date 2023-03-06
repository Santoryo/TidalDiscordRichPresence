import os
from os import system
from simple_colors import *
import tidallib
import discord
import time

state = True


print('hello')


def main(state):
    discord.connectRPC()
    system("title " + "TIDAL Rich Presence")
    _song = ""
    _artist = ""

    while True:
        artist = tidallib.artist()
        song = tidallib.song()


        print(_song, _artist)
        message = ""

        if (song != "There is nothing playing at this moment" and (song != _song or wasPaused == True)):
            message = blue("Song has changed, updating Rich Presence")
            wasPaused = False
            _song = song
            _artist = artist

            try:
                discord.updateRPC(f"{artist} - {song}")
            except:
                message = red('[ERROR] Problem with updating')

        elif(song == "There is nothing playing at this moment" and _song):
            wasPaused = True

            try:
                discord.clearRPC()
            except:
                message = red('[ERROR] Problem with clearing')

        showOnScreen(song, artist, message)
        time.sleep(3)
    




def showOnScreen(song, artist, message):
    if(song != "There is nothing playing at this moment"):
        os.system('cls')
        print(f'Now playing: {green(song)} {green("by")} {green(artist)}')
        print(message)
    else:
        os.system('cls')
        print("Nothing is being played at the moment.")



main(True)