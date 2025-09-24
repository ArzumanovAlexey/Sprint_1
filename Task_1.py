total_time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_time = total_time.replace(' ', ',')
parts = total_time.split(',')

time_int = 0
number = 0

for part in parts:
    if 'h' in part:                     
        number = int(part.replace('h', ''))
        time_int += number * 60
    elif 'm' in part:                   
        number = int(part.replace('m', ''))
        time_int += number
    elif 's' in part:                   
        number = int(part.replace('s', ''))
        time_int += number // 60

print(time_int)