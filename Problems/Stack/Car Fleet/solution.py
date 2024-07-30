class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append(float(target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)