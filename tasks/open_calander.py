import webbrowser


def open_calendar():
    calendar_url = "https://calendar.google.com/"
    webbrowser.open(calendar_url)
    return "Opening Google Calendar."
