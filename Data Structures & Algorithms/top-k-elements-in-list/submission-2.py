class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n] += 1
        print(freq)

        for num, f in freq.items():
            buckets[f].append(num)
        
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        