from typing import List


def max_sum(nums: List[int], k: int):
    max_s = 0
    n = len(nums)
    cumulative_sum = [0] * (n + 1)

    for i in range(n):
        cumulative_sum[i+1] = nums[i] + cumulative_sum[i]

    print(cumulative_sum)

    for i in range(n - k + 1):
        max_s = max(max_s, cumulative_sum[i+k] - cumulative_sum[i])

    return max_s


print(max_sum([1, 5, 6, 7, 4], 3)) # Output: 18
print(max_sum([2, 1, 2, 3, 5, 5], 1)) # Output: 5