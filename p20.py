import time
class Solution:
    def isValid(self, s: str) -> bool:
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        stack = []
        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif c in close_brackets:
                if len(stack) == 0 or close_brackets.index(c) != open_brackets.index(stack.pop()):
                    return False
        return len(stack) == 0
    def test(self) -> bool:
        return self.isValid("([])")


def main():
    print(Solution().test())

if __name__ == "__main__":
    main()