# @JUDGE_ID: 973613 10189 Python

import bisect
from math import floor


class TripExpense:
    def __init__(self):
        self.expenses = []

    def add_expense(self, cents: int):
        bisect.insort(self.expenses, cents)

    def min_exchange(self) -> int:
        expsum = sum(self.expenses)
        explen = len(self.expenses)
        mean = expsum / explen
        remainder = expsum % explen

        minexp_sum = 0
        for idx, exp in enumerate(reversed(self.expenses)):
            if exp <= mean:
                break

            if idx < remainder:
                minexp_sum += exp - (floor(mean) + 1)
            else:
                minexp_sum += exp - floor(mean)
        return minexp_sum


if __name__ == '__main__':
    from sys import stdin

    trips = []
    students = 0
    trip_start = False

    lines = stdin.read()
    for line in lines.splitlines():
        line = line.strip()

        if students > 0:
            if trip_start:
                trips.append(TripExpense())
                trip_start = False

            cent = int(float(line) * 100)
            trips[-1].add_expense(cent)

            students -= 1
            continue

        students = int(line)
        trip_start = True

        if students == 0:
            break

    for trip in trips:
        min_dollars = float(trip.min_exchange()) / 100
        print('${:.2f}'.format(min_dollars))
