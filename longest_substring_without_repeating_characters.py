class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_arr=""
        l_dict={}
        a=len(s)
        left=0
        right=0
        max_len=[]
        while right<a :
            if s[right] in left_arr:
                left=l_dict[s[right]]
                left_arr=left_arr[left+1:]
                left+=1
            left_arr+=s[right]
            l_dict[s[right]]=right
            diff=right-left+1
            max_len.append(diff)
            right+=1
        c=0
        for x in max_len:
            d=x
            if d>c:
                c=d
        return c
    
sol=Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))