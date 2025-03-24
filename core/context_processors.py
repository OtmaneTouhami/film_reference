from datetime import datetime

def add_current_date(request):
    return {
        'current_date': datetime.now(),
    }