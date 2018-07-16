DAYS_IN_MONTH = [
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31,
]

WEEKDAYS = [
    'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT',
]

month, day = list(map(lambda s: int(s), input().strip().split()))

totaldays = sum(DAYS_IN_MONTH[:(month-1)]) + day
weekday = totaldays % 7
print(WEEKDAYS[weekday])
