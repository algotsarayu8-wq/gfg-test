class Solution:
    def smallestSubstring(self, s):
        count = {'0': 0, '1': 0, '2': 0}
        
        left = 0
        min_len = float('inf')
        
        for right in range(len(s)):
            # include current character
            if s[right] in count:
                count[s[right]] += 1
            
            # shrink window if valid
            while count['0'] > 0 and count['1'] > 0 and count['2'] > 0:
                min_len = min(min_len, right - left + 1)
                
                # remove left character
                if s[left] in count:
                    count[s[left]] -= 1
                left += 1
        
        return min_len if min_len != float('inf') else -1