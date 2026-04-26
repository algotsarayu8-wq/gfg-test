class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        ans = []
        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i +=1
                j +=1
                k +=1
            else:
                m = min(a[i], b[j], c[k])
                if a[i] == m:
                    i += 1
                elif b[j] == m:
                        j += 1
                else:
                    k += 1
        return ans            