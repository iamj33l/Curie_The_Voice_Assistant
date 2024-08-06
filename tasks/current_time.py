from datetime import datetime


def get_time():
    today = datetime.now()
    return f"The current time is {today.strftime('%H:%M:%S')}."
