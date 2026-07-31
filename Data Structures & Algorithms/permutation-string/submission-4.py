class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def idx(ch):
            return ord(ch) - ord('a')
            
        # Edge case, impossible for s1 to be within s2
        if len(s1) > len(s2):
            return False

        # frequency table of s1
        window_length = len(s1)
        freq_s1 = [0] * 26
        for ch in s1:
            freq_s1[idx(ch)] += 1

        # frequency table of the window of length s1
        window = [0] * 26
        # Init the table
        for i in range(window_length):
            window[idx(s2[i])] += 1
        # init case
        if window == freq_s1:
            return True

        # sliding window
        l = 0
        for r in range(window_length, len(s2)):
            window[idx(s2[l])] -= 1
            window[idx(s2[r])] += 1
            l += 1
            if window == freq_s1:
                return True
        
        return False