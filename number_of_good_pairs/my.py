from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        # A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count

# [1, 2, 3, 4, 3, 2]

solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3])) # 4