from typing import List
from collections import defaultdict


def most_frequent_diff(nums: List[int]) -> int:
    freq_map = defaultdict(int)
    most_frequent_diff_cnt = 0

    for i in range(len(nums)-1):
        # 隣り合う要素の差の絶対値を計算
        diff = abs(nums[i+1] - nums[i])
        freq_map[diff] += 1
        # 出現頻度が現在の最頻値を上回ったら更新
        most_frequent_diff_cnt = max(most_frequent_diff_cnt, freq_map[diff])

    return most_frequent_diff_cnt


print(most_frequent_diff([1, 2, 3, 2, 1]))
print(most_frequent_diff([1, 5, 2, 3, 6]))