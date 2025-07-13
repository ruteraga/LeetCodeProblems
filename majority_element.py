class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a=[]
        b=0
        x=0
        for i in nums:
            if i not in a:
                a.append(i)
        for i in range(len(a)):
            j=nums.count(a[i])
            if j>b:
                b=j
                x=a[i]
        return x

sol=Solution()
print(sol.majorityElement([3,2,3]))