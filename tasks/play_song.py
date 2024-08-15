import threading
import pywhatkit


def play_song(song_name):
    def play():
        pywhatkit.playonyt(song_name)

    play_thread = threading.Thread(target=play)
    play_thread.start()

    return f'Playing {song_name} on YouTube.'