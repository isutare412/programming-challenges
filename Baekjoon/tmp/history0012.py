from math import gcd


def lcm(x, y):
    res = (x * y) // gcd(x, y)
    return res


class CainCalendar:
    def __init__(self, m, n):
        self._m = m
        self._n = n

    def since_origin(self, x, y):
        if self._m > self._n:
            return self._since_origin(self._m, self._n, x, y)
        else:
            return self._since_origin(self._n, self._m, y, x)

    @classmethod
    def _since_origin(cls, m, n, x, y):
        day = x
        y_wannabe = cls.step_n(n, 0, x)
        for _ in range(lcm(m, n) // m):
            if y == y_wannabe:
                return day
            day += m
            y_wannabe = cls.step_n(n, y_wannabe, m)
        return -1

    @staticmethod
    def step_n(max_, num, n):
        mod = (num + n) % max_
        return mod == 0 and max_ or mod


if __name__ == '__main__':
    size = int(input())
    for _ in range(size):
        m, n, x, y = [int(w) for w in input().split()]
        print(CainCalendar(m, n).since_origin(x, y))
