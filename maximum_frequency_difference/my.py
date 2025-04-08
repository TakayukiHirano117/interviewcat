from typing import List
from collections import defaultdict

def most_frequency(nums: List[int]) -> int:
    freq_map = defaultdict(int)
    most_frequent_diff_cnt = 0

    for i in range(len(nums)-1):
        diff = abs(nums[i+1] - nums[i])
        freq_map[diff] += 1
        most_frequent_diff_cnt = max(most_frequent_diff_cnt, freq_map[diff])

    return most_frequent_diff_cnt

print(most_frequency([1, 2, 3, 2, 1]))
print(most_frequency([1, 5, 2, 3, 6]))