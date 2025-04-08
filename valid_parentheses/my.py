def is_valid_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # スタックが空（つまり対応する開き括弧がない）または、
            # スタックのトップの要素が開き括弧でなければ、Falseを返します
            if not stack or stack.pop() != '(':
                return False
    # 文字列のすべての文字をチェックした後、スタックが空であればTrueを返します。
    # これは、すべての開き括弧に対応する閉じ括弧が存在したことを意味します。
    return len(stack) == 0

print(is_valid_parentheses("()")) # Output: True
print(is_valid_parentheses("(())")) # Output: True
print(is_valid_parentheses("(())()")) # Output: True
print(is_valid_parentheses("(())(")) # Output: False
print(is_valid_parentheses("(()")) # Output: False
print(is_valid_parentheses("())")) # Output: False


# leetcode
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != '(':
                    return False
            elif char == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif char == "]":
                if not stack or stack.pop() != "[":
                    return False

        return len(stack) == 0