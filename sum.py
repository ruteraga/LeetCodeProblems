#for next try. to use recursion with a for loop 
class Solution(object):
    def threeSum(self, nums):
        dict=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                l=[]
                diff=0-(nums[i]+nums[j])
                if diff in nums:
                    k=nums.index(diff)
                    if i!=j and i!=k and j!=k:
                        l.append(nums[i])
                        l.append(nums[j])
                        l.append(nums[k])
                l.sort()
                if l not in dict and len(l)!=0:
                    dict.append(l)
            nums.pop(i)
        return threeSum(nums)

sol=Solution()
l=[-1,0,1,2,-1,-4]
print(sol.threeSum(l))