# https://leetcode.com/problems/validate-stack-sequences/description://leetcode.com/problems/validate-stack-sequences/description/

# popped.length == pushed.length
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for elem in pushed:
            stack.append(elem)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack  # t/f
