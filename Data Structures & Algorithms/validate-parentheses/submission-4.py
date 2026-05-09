class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 != 0:
        #     return False
        # if len(s) == 0:
        #     return True
        # if s[0] in ')}]':
        #     return False
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        curr = []
        for ch in s:
            if ch in '({[':
                curr.append(ch)
            elif ch in ')}]':
                if len(curr) == 0:
                    return False
                elif curr[-1] != mapping[ch]:
                    return False
                curr.pop()
        return not curr
