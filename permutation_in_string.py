class Solution(object):
    def checkInclusion(self, s1, s2):
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        sorted_s1 = sorted(s1)
        for left in range(len_s2 - len_s1 + 1):
            arr = s2[left:left + len_s1]
            if sorted_s1 == sorted(arr):
                return True
        return False
    
sol=Solution()
print(sol.checkInclusion('ab','eidbaooo'))