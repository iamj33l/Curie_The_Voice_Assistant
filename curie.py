from speech import SpeechModule
from tasks.current_time import get_time
from tasks.current_date import get_date
from tasks.find_place import find_place
from tasks.open_app import open_app
from tasks.open_calander import open_calendar
from tasks.play_song import play_song
from tasks.search_google import search_google


class Curie:

    def __init__(self):
        self.speech = SpeechModule()

    def start(self):
        self.speech.synthesize_speech("Hello, I am Curie. How can I help you today?")
        self.speech.recognize_speech_from_mic()

    def execute(self, command):

        if "hello" in command.lower() or "hi" in command.lower():
            self.speech.synthesize_speech("Hello, how can I help you today?")

        elif "current time" in command.lower():
            response = get_time()
            self.speech.synthesize_speech(response)

        elif "current date" in command.lower():
            response = get_date()
            self.speech.synthesize_speech(response)

        elif "open" in command.lower():
            app_name = command.split("open")[1].strip()
            response = open_app(app_name)
            self.speech.synthesize_speech(response)

        elif "play" in command.lower():
            song_name = command.split("play")[1].strip()
            response = play_song(song_name)
            self.speech.synthesize_speech(response)

        elif "search" in command.lower():
            query = command.split("search")[1].strip()
            response = search_google(query)
            self.speech.synthesize_speech(response)

        elif "find" in command.lower():
            place = command.split("find")[1].strip()
            response = find_place(place)
            self.speech.synthesize_speech(response)

        elif "open calendar" in command.lower():
            response = open_calendar()
            self.speech.synthesize_speech(response)

        else:
            self.speech.synthesize_speech("Sorry, I did not understand that command.")
