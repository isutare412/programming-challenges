got_str = input()
a, b, c = list(map(lambda s: int(s), got_str.strip().split()))
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)