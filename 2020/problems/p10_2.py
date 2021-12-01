from collections import Counter
from functools import lru_cache


with open('../data/p10_data.txt', "r") as f:
    adapters = list(map(int, f.readlines()))
adapters = sorted(adapters + [0, max(adapters) + 3])

diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
hist = Counter(diffs)

print(f"Part 1: {hist[1] * hist[3]}")


@lru_cache(maxsize=256)
def paths_to_end(i):
    if i == len(adapters) - 1:
        return 1
    return sum(
        [
            paths_to_end(j)
            for j in range(i + 1, min(i + 4, len(adapters)))
            if adapters[j] - adapters[i] <= 3
        ]
    )


print(f"Part 2: {paths_to_end(0)}")