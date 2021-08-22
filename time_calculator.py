def add_time(start, duration, day=''):
    # Split the times so we can add hours and minutes

    start_splitted = start.split(':')
    minutes = start_splitted[1].split()
    hours_mins_half = [start_splitted[0], minutes[0], minutes[1]]
    duration = duration.split(':')

    hours = int(hours_mins_half[0]) + int(duration[0])
    minutes = int(hours_mins_half[1]) + int(duration[1])
    half_of_day = hours_mins_half[2]

    daycount = 0
    day = day.lower()

    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1

    # Formatting time
    while hours > 12:
        if hours > 12 and half_of_day == 'PM':
            half_of_day = 'AM'
            hours = hours - 12
            daycount = daycount + 1

        elif hours > 12 and half_of_day == 'AM':
            half_of_day = 'PM'
            hours = hours - 12

    if hours == 12 and half_of_day == 'PM':
        half_of_day = 'AM'
        daycount = daycount + 1

    elif hours == 12 and half_of_day == 'AM':
        half_of_day = 'PM'

    # used to iterate through the list and find the correct day (x days later)
    daylist = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day in daylist:
        day_index = daylist.index(day.lower())
        dcount = daycount
        while dcount > 0:
            if day_index >= 6:
                day_index = day_index - 7
            day_index = day_index + 1
            dcount = dcount - 1

    # Formatting the string, a lot of if else

    if daycount == 0 and day != '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) +
                    " " + half_of_day.upper() + ', ' + day.capitalize())
    elif daycount == 0 and day == '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) +
                    " " + half_of_day.upper())
    elif daycount == 1 and day != '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) + " " +
                    half_of_day.upper() + ', ' + daylist[day_index].capitalize() + ' (next day)')
    elif daycount == 1 and day == '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) +
                    " " + half_of_day.upper() + ' (next day)')
    elif daycount > 1 and day != '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) + " " +
                    half_of_day.upper() + ', ' + daylist[day_index].capitalize() + " (" + str(daycount) + ' days later)')
    elif daycount > 1 and day == '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) + " " +
                    half_of_day.upper() + " (" + str(daycount) + ' days later)')

    return new_time.rstrip()

