class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=""
        #l_dict={}
        a=len(s)
        max_len=[]
        for word in s:
            if word in arr:
                left=arr.index(word)
                arr=arr[left+1:]
            arr+=word
            diff=len(arr)
            max_len.append(diff)
            print(arr)
        c=0
        print(max_len)
        for x in max_len:
            if x>c:
                c=x
        return c
    
sol=Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))