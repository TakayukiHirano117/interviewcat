# nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4, 6]

flag = False

# numsのi番目以降の部分配列を取得し、
# そこにnums[i]が含まれていたらTrueを出力
# Ex. i = 1の場合、nums[i+1:] は [2,3,1]
for i in range(len(nums)):
    if nums[i] in nums[i+1:]:
        flag = True
        break

print(flag)

# 以下は普通に二重ループしたとき
# for i in range(len(nums)):
#     for j in range(len(nums)):
#     for j in range(len(nums)):はi+1, len(nums)にすればいい
#         if i == j:
#             continue
#         else: 
#             nums[i] == nums[j]:
#             flag = True
#             break

# print(flag)
# https://chatgpt.com/c/67b5afe6-05ec-8008-ad6b-1d8ff0e0c5ac