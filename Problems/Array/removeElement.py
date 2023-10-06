def removeElement(nums, val):
    nums[:] = [x for x in nums if x != val]
    return len(nums)


def main():
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))


main()
