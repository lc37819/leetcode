class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        Map = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in Map:
                topElement = stack.pop() if stack else "#"
                if Map[c] != topElement:
                    return False
            else:
                stack.append(c)
        return not stack