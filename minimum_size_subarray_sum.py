class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        right=0
        diff=0
        minimum=[]
        arr=[]
        sum=0
        while left<=right:
            if sum>=target:
                diff=right-left
                arr.append(diff)
                sum-=minimum[0]
                minimum.pop(0)
                left+=1
            else:
                if right>=len(nums):
                    break
                else:
                    sum+=nums[right]
                    minimum.append(nums[right])
                    right+=1
        if len(arr)==0:
            mi=0
        else:
            mi=min(arr)
        return mi
    
sol=Solution()
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))