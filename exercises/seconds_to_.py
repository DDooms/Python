def seconds_to_time(seconds):
    hours = 0
    minutes = 0
    counting_seconds = 0
    for second in range(seconds):
        counting_seconds += 1
        if counting_seconds == 60:
            minutes += 1
            counting_seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0

    return hours, minutes, counting_seconds


print(seconds_to_time(86399))
