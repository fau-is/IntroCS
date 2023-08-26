from datetime import datetime
import pytz

class TimeTrigger():
    def __init__(self, ptime):
        format = '%Y-%m-%d %H:%M:%S%z'
        ptime = datetime.strptime(ptime, format)
        ptime = ptime.replace(tzinfo=pytz.timezone("EST"))
        self.ptime = ptime
        
if __name__ == '__main__':
    trigger = TimeTrigger('2023-07-22 09:37:34+00:00')
    print(trigger.ptime)