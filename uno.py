def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    hour_str = str(hour).rjust(2, '0')
    minute_str = str(minute).rjust(2, '0')
    
    return hour_str + minute_str
