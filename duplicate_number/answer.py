from typing import List


def has_duplicate(nums: List[int]) -> bool:
    # nums[i]とnums[j]のネストしたfor-loopで比較
    for i in range(len(nums)):
        # 自分自身をいれる必要はないのでi+1から始める
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


print(has_duplicate([1, 2, 3, 1]))
print(has_duplicate([1, 2, 3, 4, 6]))