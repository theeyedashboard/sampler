from dateutil import rrule
from datetime import datetime, timedelta
import json


class Sampler:

    def __init__(self):
        self.date_min = datetime.now() - timedelta(days=7)
        self.date_max = datetime.now()
        self.growth   = 1
        return None

    def extract(self):
        output = {}
        value  = 0
        timetable = rrule.rrule(rrule.HOURLY, dtstart=self.date_min, until=self.date_max)
        output['count'] = format(timetable.count())
        samples = []
        for dt in timetable:
            sample = {'date':format(dt), 'value':round(value)}
            samples.append(sample)
            value += self.growth
        output['samples'] = samples
        # return json.dumps(output)
        return output
