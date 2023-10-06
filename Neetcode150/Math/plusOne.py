# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(digits):
        digits = digits[::-1]  # reversed (easier to code)
        carry, i = 1, 0
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    # carry = 1
                else:
                    digits[i] += 1
                    carry = 0
            else:  # out of bounds : all digits over : add carry to it
                digits.append(carry)
                carry = 0
            i += 1
        return digits[::-1]


if __name__ == "__main__":
    digits = [1, 2, 3]
    print(Solution.plusOne(digits))
