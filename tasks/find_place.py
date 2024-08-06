import webbrowser


def find_place(place_name):
    search_url = f"https://www.google.com/maps/search/{place_name}"
    webbrowser.open(search_url)
    return f"Searching for {place_name} on Google Maps."
