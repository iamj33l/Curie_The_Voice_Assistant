import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
from curie import Curie


class CurieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Curie")

        self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled', width=50, height=20)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10)

        self.speak_button = tk.Button(self.root, text="Speak", command=self.activate_voice_assistant)
        self.speak_button.grid(row=1, column=0, pady=10)

        self.curie = Curie()
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def activate_voice_assistant(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.update_chat_history("Curie: How can I help you today?")
            audio = self.recognizer.listen(source)

        try:
            user_input = self.recognizer.recognize_google(audio)
            self.update_chat_history(f"User: {user_input}")
            response = self.curie.execute(user_input)
            self.update_chat_history(f"Curie: {response}")
        except sr.UnknownValueError:
            self.update_chat_history("Curie: Sorry, I did not understand that.")
        except sr.RequestError:
            self.update_chat_history("Curie: Sorry, my speech service is down.")

    def update_chat_history(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CurieApp(root)
    root.mainloop()
