#Challenge 1: Converting 12-hour time to 24-hour time

def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    hour_str = str(hour).rjust(2, '0')
    minute_str = str(minute).rjust(2, '0')
    
    return hour_str + minute_str

time_1 = convert_to_24_hour(8, 30, "am")
print(time_1)  #Output 0830

time_2 = convert_to_24_hour(8, 30, "pm")
print(time_2)  #Output 2030
