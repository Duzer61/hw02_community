import datetime as dt


def year(request):
    """Добавляет переменную с текущим годом."""
    date = int(dt.datetime.today().strftime('%Y'))
    return {
        'year': date
    }
