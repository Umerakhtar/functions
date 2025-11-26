import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
if hour < 12:
    print('Good Morning')
elif 12 <= hour < 18:
    print('Good Afternoon')
else:
    print('Good Evening')

print('Current Time is :', t)