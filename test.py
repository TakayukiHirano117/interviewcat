# sliding window

# その後、windowの左端を1つずつ右にずらしながら、それぞれ合計を求める
# その中で最大の合計を求める

from typing import List


def get_max_sum_in_window(nums: List[int], k: int) -> bool:
    cur_sum = 0
    max_sum = 0
    
    # 最初にkの長さ文のwindow分の合計を求める
    for i in range(k):
        cur_sum += nums[i]
    # 初期Windowでの合計値を現在の最大とします
    max_sum = cur_sum

    for i in range(k, len(nums)):
        # Windowの左端の数字を引きます
        cur_sum -= nums[i-k]
        # Windowの右端に新しい数字を加えます
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)

    return max_sum 



def sliding_window(nums: List[int], k: int) -> bool:
    cur_sum = 0
    max_sum = 0

    for i in range(k):
        cur_sum += nums[i]
        max_sum = cur_sum

    for i in range(k, len(nums)):
        cur_sum -= nums[i-k]
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)

    return max_sum
