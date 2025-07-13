class Solution:  
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        n1=[]
        n2=[]
        nums=[]
        n1=nums1[:m]
        n2=nums2[:n]
        left=len(n1)
        right=len(n2)
        if right ==0 :
            return
        nums1.clear()
        i,j=0,0
        while i<left and j<right:
            if n1[i]<=n2[j]:
                nums1.append(n1[i])
                i+=1
            else:
                nums1.append(n2[j])
                j+=1
        if i<left:
            nums1.extend(n1[i:])
        if j<right:
            nums1.extend(n2[j:])
        print(nums1)
Sol=Solution()
Sol.merge([1,2,3,0,0,0],3,[2,5,6],3)