import speech_recognition as sr
import pyttsx3

class SpeechModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def recognize_speech_from_mic(self):
        """Recognize speech from the microphone and return it as text."""
        with sr.Microphone() as source:
            print("Please say something:")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def synthesize_speech(self, text):
        """Synthesize speech from text."""
        self.change_voice(1)
        self.engine.say(text)
        self.engine.runAndWait()

    def change_voice(self, voice_id):
        """Change the voice of the speech synthesizer."""
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_id].id)

    def set_speech_rate(self, rate):
        """Set the speech rate of the synthesizer."""
        self.engine.setProperty('rate', rate)

    def set_volume(self, volume):
        """Set the volume of the synthesizer."""
        self.engine.setProperty('volume', volume)
