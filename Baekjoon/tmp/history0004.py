BIG_BAG = 5
SMALL_BAG = 3
BAG_FAIL = -1

sugarmass = int(input())

big_num = sugarmass // BIG_BAG
small_num = 0
smallbag_mass = sugarmass % BIG_BAG

result = BAG_FAIL
while big_num >= 0:
    if smallbag_mass % SMALL_BAG == 0:
        small_num = smallbag_mass // SMALL_BAG
        result = big_num + small_num
        break

    big_num -= 1
    smallbag_mass += BIG_BAG

print(result)
