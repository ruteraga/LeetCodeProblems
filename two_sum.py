class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a=len(nums)
        res=[]
        for i in range(a):
            b=target-nums[i]
            if b in nums:
                c=nums.index(b)
            if b in nums and i not in res and c!=i:
                res.append(i)
                res.append(c)
        return res
    
sol=Solution()
print(sol.twoSum([2,7,11,15],9))