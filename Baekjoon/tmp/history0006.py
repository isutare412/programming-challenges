height = int(input())

for i in range(height, 0, -1):
    print(' ' * (height - i), end='')
    print('*' * i)
