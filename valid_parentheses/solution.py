class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_parentheses = set(['(', '{', '['])
        parentheses_matches = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        for i in range(len(s)):
            # 開き括弧ならstackに積む
            if s[i] in open_parentheses:
                st.append(s[i])
            else:
                # 閉じ括弧が来た場合にそれと対応するものがstackのトップにいるかを確認
                if st and parentheses_matches[s[i]] == st[-1]:
                    # 対応が確認できたので、stackから取り出す
                    st.pop()
                else:
                    # 対応開き括弧いない場合は即座にreturn
                    return False
        
        return len(st) == 0