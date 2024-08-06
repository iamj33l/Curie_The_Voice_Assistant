from datetime import datetime


def get_date():
    today = datetime.now()
    return f"Today's date is {today.strftime('%Y-%m-%d')}."
