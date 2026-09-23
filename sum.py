class Solution(object):

  def threeSum(self, nums):
    res = []
    nums.sort()  # Step 1: Sort the array

    for i in range(len(nums)):
      # Skip duplicates for the first number to avoid duplicate triplets
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # Step 2: Use two pointers for the remaining elements
      left, right = i + 1, len(nums) - 1

      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if current_sum < 0:
          left += 1  # Sum is too small, move the left pointer up
        elif current_sum > 0:
          right -= 1  # Sum is too large, move the right pointer down
        else:
          res.append([nums[i], nums[left], nums[right]])
          left += 1
          right -= 1

          # Skip duplicates for the second and third numbers
          while left < right and nums[left] == nums[left - 1]:
            left += 1
          while left < right and nums[right] == nums[right + 1]:
            right -= 1

    return res


# Test the solution
sol = Solution()
l = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(l))