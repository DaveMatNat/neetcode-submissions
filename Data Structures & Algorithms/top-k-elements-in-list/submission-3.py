class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] += 1
        
        for num, f in count.items():
            freq[f].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res