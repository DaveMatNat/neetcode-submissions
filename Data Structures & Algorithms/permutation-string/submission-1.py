class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s2) < len(s1):
            return False
        # frequency table of s1
        window_length = len(s1)
        freq_s1 = [0] * 26
        for ch in s1:
            index = ord(ch)-ord('a')
            freq_s1[index] += 1

        # frequency table of the window of length s1
        window = [0] * 26
        # Init the table
        for i in range(window_length):
            index = ord(s2[i])-ord('a')
            window[index] += 1
        # init case
        if window == freq_s1:
            return True
        print(window)
        # sliding window
        l = 0
        for r in range(window_length, len(s2)):
            # deal left
            index = ord(s2[l])-ord('a')
            window[index] -= 1
            l += 1
            # deal right
            index = ord(s2[r])-ord('a')
            window[index] += 1
            if window == freq_s1:
                return True
        
        return False