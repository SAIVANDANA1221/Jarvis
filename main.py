# import os
import eel

from engine.features import *
from engine.command import *


def start():
    eel.init("www")
    playAssistantSound()
   
    # Open the application in Chrome browser in "app" mode
    eel.start('index.html', mode='chrome', host='localhost', port=8000)

if __name__ == "__main__":
    start()