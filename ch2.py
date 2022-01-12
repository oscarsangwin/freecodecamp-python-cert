days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
mins_in_day = 60 * 24

def clock_to_mins(time_full):
    """Converts 12-hr clock string to number of seconds since midnight"""

    time, half = time_full.split() # '12:00 AM' -> '12:00', 'AM' 
    hr, mins = [int(x) for x in time.split(':')] # '12:00' -> 12, 00

    if half == 'AM':
        # Morning
        if hr == 12:
            return mins
        else:
            return hr * 60 + mins
    else:
        # Afternoon
        if hr == 12:
            return 12 * 60 + mins
        else:
            return 12 * 60 + hr * 60 + mins

def mins_to_clock(mins):
    """Converts number of seconds since midnight to 12-hr clock string"""

    # Get which half of day (ie AM or PM) and the minutes in that half
    half, mins_since_half = divmod(mins, (60 * 12))

    # Split into hours and minutes
    hr, mins = divmod(mins_since_half, 60)
    if hr == 0:
        hr = 12
    mins = str(mins).rjust(2, '0') # 3 -> '03'

    if half:
        # Afternoon
        return f'{hr}:{mins} PM'
    else:
        # Morning
        return f'{hr}:{mins} AM'

def add_time(start, duration, *args):

    # Optional show day parameter
    if args:
        day = args[0].lower()
    else:
        day = False
    
    # Convert inputs to min and get new time
    start_mins = clock_to_mins(start)
    hr, mins = [int(x) for x in duration.split(':')]
    new_mins = start_mins + hr * 60 + mins

    # Get time of day in 12-hr format of new time
    days_passed, day_mins = divmod(new_mins, mins_in_day)

    # Convert back to 12-hr format
    new_time_str = mins_to_clock(day_mins)

    # Optional day of week
    if day:
        index = days.index(day)
        index = (index + days_passed) % len(days)
        new_time_str += f', {days[index].capitalize()}'

    # Brackets part if new time is not on the same day
    if days_passed == 1:
        new_time_str += ' (next day)'
    elif days_passed > 1:
        new_time_str += f' ({days_passed} days later)'

    return new_time_str