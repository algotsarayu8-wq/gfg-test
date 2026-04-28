class Solution:
    def longestSubstr(self, s, k):
        freq = [0]*26
        left = 0
        maxfreq = 0
        ans = 0

        for right in range(len(s)):
            index = ord(s[right])-ord('A')
            freq[index] +=1
            maxfreq = max(maxfreq,freq[index])
            while (right-left+1)-maxfreq > k:
                freq[ord(s[left])-ord('A')] -= 1
                left += 1

            ans = max(ans, right-left+1)

        return ans
       