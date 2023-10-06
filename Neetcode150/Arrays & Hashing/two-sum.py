# https://leetcode.com/problems/two-sum/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# approach -> keep a hashmap, go through elements (a + b = c, so c - b = a)
# if present in hashmap -> answer found, else keep adding elements to hashmap.

def twoSum(arr, target):
    hashmap = {}  # {value_of_nums, index}
    for index, val in enumerate(arr):
        if target - val in hashmap:
            return [hashmap[target - val], index]  # index return
        hashmap[val] = index  # else add to hashmap


def main():
    print(twoSum(arr=[2, 7, 8, 13, 45], target=9))


main()
