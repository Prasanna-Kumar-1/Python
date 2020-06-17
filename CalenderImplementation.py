import calendar
print(calendar.month(2018, 6))

print("-" * 40)

print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2020, 2, 1, 1, 2))

print("-" * 40)

for name in calendar.month_name:
    print(f'Name of the Month is : {name}')

print("-" * 40)

for day in calendar.day_name:
    print(f'Name of the Month is : {day}')

print("-" * 40)

# Show every month
for month in range(1, 13):

    # Compute the dates for each week that overlaps the month
    c = calendar.monthcalendar(2020, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    # If there is a Thursday in the first week, the second Thursday
    # is in the second week.  Otherwise the second Thursday must
    # be in the third week.
    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print(f'Meeting date in the month {month} is {meeting_date}'.format(month, meeting_date))