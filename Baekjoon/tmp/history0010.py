def mean(list_):
    return sum(list_) / len(list_)


test_size = int(input())

for _ in range(test_size):
    size, *scores = list(map(lambda s: int(s), input().strip().split()))
    score_mean = mean(scores)

    above_mean = sum(1 for s in scores if s > score_mean)
    ratio = above_mean / size
    print('{:.3f}%'.format(ratio * 100))
