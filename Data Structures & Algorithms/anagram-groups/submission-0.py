class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            fingerprint = [0] * 26
            for c in s:
                fingerprint[ord(c) - ord('a')] += 1
            res[tuple(fingerprint)].append(s)
        return list(res.values())