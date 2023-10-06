# //leetcode.com/problems/subarray-sums-divisible-by-k/description/
def subarraysDivByK(nums, k):
    res = 0
    prefix = 0
    # count is a list and not a dictionary (lists are faster than dictionaries)
    count = [1] + [0] * k  # [1, 0, 0, 0, 0, 0]
    for num in nums:
        prefix = (prefix + num) % k
        res += count[prefix]  # 2 + 1 + 4 = 7
        count[prefix] += 1  # if same found ([2, 0, 1, 0, 4, 0])


def main():
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(subarraysDivByK(nums, k))


main()
