import threading
import pywhatkit as kit


def play_song(song_name):
    def play():
        kit.playonyt(song_name)

    play_thread = threading.Thread(target=play)
    play_thread.start()

    return f'Playing {song_name} on YouTube.'
