import sys
from functools import reduce

length = int(sys.stdin.readline().rstrip())

for i in range(length):
    sum_ = reduce(
        lambda a, b: int(a) + int(b),
        sys.stdin.readline().rstrip().split()
    )
    print(sum_)
