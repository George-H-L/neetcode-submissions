class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in '({[':
                seen.append(i)
            else:
                if not seen or seen[-1] != pairs[i]:
                    return False
                seen.pop()

        return not seen



            