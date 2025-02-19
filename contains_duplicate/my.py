from collections import defaultdict
from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         flag = False
#         freq_map = defaultdict(int)
#         for i in range(len(nums)):
#             freq_map[nums[i]] += 1
        
#         for i in range(len(freq_map)):
#             if freq_map[i] > 1:
#                 flag = True
#                 break
        
#         return flag
    
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4]))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return True
        return False