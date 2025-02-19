from heapq import heapify, heappush, heappop

ary = [1, 5, 8, 0, 2, 6, 3, 9, 10, 4, 7, 11]

# Nをheapとaryのサイズとする
# (1) heapify: O(N)
heapify(ary)
heap = ary
print(heap)
# heap = [0, 1, 3, 5, 2, 6, 8, 9, 10, 4, 7, 11]
# Min Heapであることに注意！
# 小さい順に優先度が高い

# (2) heappush: O(log N)
# 5を新しい要素として追加
heappush(heap, 5)
print(heap)
# heap = [0, 1, 3, 5, 2, 5, 8, 9, 10, 4, 7, 11, 6]

# (3) heappop: O(log N)
# 最長値を取り出す
minimum = heappop(heap)
print(minimum)
print(heap)
# minimum = 0
# heap = [1, 2, 3, 5, 4, 5, 8, 9, 10, 6, 7, 11]