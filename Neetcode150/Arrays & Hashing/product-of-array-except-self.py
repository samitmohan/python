# https://leetcode.com/problems/product-of-array-except-self/

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

'''
Documentation
  The trick here is to use two passes -> complexity of O(n) means taht we can do two loops remember ?
  First, we compute the prodcut in the first pass, we keep the val of the first pas and mult withthe val.
  We do the same at the second pass

TC -> O(N), SC -> O(N) [Can be improved to O(1))
Logic -> [1,2,3,4] -> except arr[i] multiply left_part_of_arr * right_part_of_arr and do this for all elements 
Case -> first and last number (of left and right resp) should always be 1 so to avoid multiplication by 0. 
'''


class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        # variable declaration
        size = len(arr)
        left_prod = [0] * size
        right_prod = [0] * size
        op = [0] * size

        # default val
        left_prod[0] = 1
        right_prod[size - 1] = 1;

        # left
        for i in range(1, size):
            left_prod[i] = arr[i - 1] * left_prod[i - 1]

        # right
        for i in range(size - 2, -1, -1):  # goes till 0
            right_prod[i] = arr[i + 1] * right_prod[i + 1]

        # final
        for i in range(size):
            op[i] = left_prod[i] * right_prod[i]

        return op


# alt solution -> O(1) Space
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    first_pass = 1
    for i in range(len(nums)):
        res[i] = first_pass
        first_pass *= nums[i]

    second_pass = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= second_pass
        second_pass *= nums[j]

    return res
