class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # "s"と"t"の長さが異なる場合、"t"は"s"のアナグラムにはなり得ないので、Falseを返す
        if len(s) != len(t):
            return False

        # 小文字英字の各文字の出現回数のカウンター
        counter = [0] * 26

        # "s"と"t"の各文字についてループを行う
        for i in range(len(s)):
            # "s"の各文字の出現回数をカウントアップする
            counter[ord(s[i]) - ord('a')] += 1
            # "t"の各文字の出現回数をカウントダウンする
            counter[ord(t[i]) - ord('a')] -= 1

        # 出現回数のリストをループし、出現回数が0でない文字があるかチェックする
        for count in counter:
            # 出現回数が0でない（すなわち"s"と"t"で出現回数が一致しない）文字がある場合、Falseを返す
            if count != 0:
                return False

        # すべての文字の出現回数が一致（つまり"s"と"t"がアナグラム）である場合、Trueを返す
        return True