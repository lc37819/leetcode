class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            frequency[c].append(n)
        
        result = []
        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result