import threading
import pywhatkit as kit

def search_google(query):
    def search():
        kit.search(query)

    search_thread = threading.Thread(target=search)
    search_thread.start()
    return f"Searching Google for {query}."