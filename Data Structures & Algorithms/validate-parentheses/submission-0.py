class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in my_dict:
                stack.append(char)
            else:
                if not stack or my_dict[stack.pop()] != char:
                    return False
        return len(stack) == 0