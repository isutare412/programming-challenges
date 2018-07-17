def triangle_helper(height, row):
    if height == 3:
        if row == 0:
            return '  *'
        elif row == 1:
            return ' * *'
        else:
            return '*****'

    half = height // 2
    if row < half:
        return ' ' * half + triangle_helper(half, row)
    else:
        fixedrow = row - half
        substr = triangle_helper(half, fixedrow)
        return substr + ' ' * (half - fixedrow) + substr


def triangle(height):
    for i in range(height):
        yield triangle_helper(height, i)


height = int(input())
for row in triangle(height):
    print(row)
