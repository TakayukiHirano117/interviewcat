from typing import List


def is_rotated(matrix: List[List[int]], target: List[List[int]]) -> bool:
    n = len(matrix)
    # print(n)
    for i in range(n):
        for j in range(n):
            # matを時計回りに90度回転させると、mat[i][j]の位置の要素は、
            # mat[j][n-i-1]の位置に移動します
            # それがtargetの対応する位置の要素と一致しない場合は、Falseを返します
            if matrix[i][j] != target[j][n-i-1]:
                return False

    return True


print(is_rotated(
    [
        [0,1],
        [1,0]
    ],
    [
        [1,0],
        [0,1]
    ]
) == True)
print(is_rotated(
    [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ],
    [
        [0,0,1],
        [0,1,0],
        [1,0,0]
    ]
) == True)
print(is_rotated(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
) == True)
print(is_rotated(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [9,8,7],
				[6,5,4],
			  [3,2,1]
    ]
) == False)
print(is_rotated(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ],
    [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
) == True)