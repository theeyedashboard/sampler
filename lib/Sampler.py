from dateutil import rrule
from datetime import datetime, timedelta

class Sampler:

    def __init__(self):
        self.date_min = datetime.now() - timedelta(days=100)
        self.date_max = datetime.now()
        return None

    def extract(self):
        output = ""
        output += 'yeah'
        return output
