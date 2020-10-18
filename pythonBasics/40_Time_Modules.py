from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta
import calendar

oggi = datetime.now()
print('Now: ', str(datetime.now()))
print('Today: ', str(date.today()))
print('Year: ', oggi.strftime('%Y'))
print('Day: ', oggi.strftime('%d'))
print('Month: ', oggi.strftime('%m'))
print('Hour: ', oggi.strftime('%H'))
print('Minutes: ', oggi.strftime('%M'))
print('Seconds: ', oggi.strftime('%S'))
print('Built date-time: ', oggi.strftime('%Y'), oggi.strftime('%m'), oggi.strftime('%d'), oggi.strftime('%H'), oggi.strftime('%S'))
print('Built date-time2: ', oggi.strftime('%Y-%m-%d_%H:%M:%S'))

print('Timedelta 24 h: ', timedelta(hours=24))
print('Date-time 24 hr ago: ', str(datetime.now() - timedelta(hours=24)))

print('Time now: ', oggi.strftime('%H:%M:%S'))

cal = calendar.TextCalendar(calendar.SUNDAY)
str = cal.formatmonth(2020, 1)
print(str)

for name in calendar.month_name:
    print(name)
