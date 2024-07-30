class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def backtrack(openN, closed):
            if openN == closed == n:
                result.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closed)
                stack.pop()
            
            if closed < openN:
                stack.append(")")
                backtrack(openN, closed+1)
                stack.pop()
        backtrack(0,0)
        return result