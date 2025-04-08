from typing import List


def has_consecutive_seq(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            return True
    return False


print(has_consecutive_seq([4, 1, 5]))
print(has_consecutive_seq([4, 1, 6]))