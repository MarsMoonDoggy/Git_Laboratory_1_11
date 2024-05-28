from datetime import datetime


def get_datetime():
    print(datetime.now().strftime('%d.%m.%y %H:%M'))
    print()