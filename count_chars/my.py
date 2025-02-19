# from collections import defaultdict

# s = "leetcode"
# d = defaultdict(int)

# for c in s:
#     d[c] += 1

# print(d)

# from collections import Counter


# def char_counts(s: str) -> Counter:
#     return Counter(s)


# print(char_counts("leetcode"))
# print(char_counts(""))

from typing import List


def char_counts(s: str) -> List[int]:
    # 英語のアルファベットは26文字あるため、配列のサイズは26です。
    counter = [0] * 26

    for i in range(len(s)):
        # 文字列sの各文字（ここでは小文字の英字のみを想定）に対して、
        # その文字が現れた回数をカウントします。
        # ord関数を使って文字をそのASCII値に変換し、
        # 'a'のASCII値を引くことでアルファベットのインデックス（0から25）を取得します。
        counter[ord(s[i]) - ord('a')] += 1

    return counter


print(char_counts("leetcode"))
print(char_counts(""))