MIN_IN_HOURS = 60 # pragma: no mutate
HOURS_IN_HALFDAY = 12 # pragma: no mutate
DEGREES_IN_SEGMENT = 30 # pragma: no mutate
DEGREES_IN_MIN = 6 # pragma: no mutate


def hours_hand(hour, minutes):
    base = (hour % HOURS_IN_HALFDAY ) * (DEGREES_IN_SEGMENT)
    correction = int((minutes / MIN_IN_HOURS) * (DEGREES_IN_SEGMENT)) 
    return base + correction

def minutes_hand(hour, minutes):
    return (minutes % MIN_IN_HOURS) * (DEGREES_IN_MIN)

def between(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(hour, minutes))