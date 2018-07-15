# @JUDGE_ID: XXXXXX 10189 Python


class MineField:
    _MINE = '*'

    def __init__(self, n: 'row', m: 'column'):
        self.ROW = n
        self.COL = m
        self.field = []
        for _ in range(n):
            self.field.append([0 for _ in range(m)])

    def __repr__(self):
        result = ''
        for m in range(self.ROW):
            for n in range(self.COL):
                result += str(self.field[m][n])
            result += '\n'
        return result

    def read_mine_by_row(self, m: int, row: str):
        for n, c in enumerate(row):
            if c == '*':
                self.plant_mine((m, n))

    def plant_mine(self, coord: 'tuple (x, y)'):
        x, y = coord
        self.field[x][y] = self.__class__._MINE
        self._flag_mine(coord)

    def _flag_mine(self, coord: 'tuple (x, y)'):
        x, y = coord
        for m in range(x-1, x+2):
            if m < 0 or m >= self.ROW:
                continue

            for n in range(y-1, y+2):
                if n < 0 or n >= self.COL:
                    continue

                if self.field[m][n] != self.__class__._MINE:
                    self.field[m][n] += 1


if __name__ == '__main__':
    from sys import stdin

    m = 1
    n = 1
    minefield_line = 0
    minefields = []

    lines = stdin.read()
    for line in lines.splitlines():
        line = line.strip()
        if minefield_line > 0:
            if minefield_line == m:
                minefields.append(MineField(m, n))

            minefields[-1].read_mine_by_row(m - minefield_line, line)
            minefield_line -= 1
            continue

        m, n = list(map(lambda num: int(num), line.split()))
        minefield_line = m

        if m == 0 and n == 0:
            break

    for idx, mfield in enumerate(minefields, 1):
        print('Field #{}:'.format(idx))
        line_end = idx != len(minefields) and '\n' or ''
        print(mfield, end=line_end)
