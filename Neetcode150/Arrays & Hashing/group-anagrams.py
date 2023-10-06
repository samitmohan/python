# https://leetcode.com/problems/group-anagrams/

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # approach -> count of the letters will be same.
        # tan / nat -> 1 a, 1 t, 1 n. Hashmap -> key [pattern], value [which strings have this pattern]
        # 1 e, 1 a, 1 t -> eat
        # m -> total number of input strings, n -> average length of a string, we're using count (len -> 26)
        # O(m * n)

        res = defaultdict(list)  # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26  # a...z
            for character in s:
                count[ord(character) - ord("a")] += 1  # for every char
            res[tuple(count)].append(s)  # group all anagrams (list are not keys -> so changed to tuple)

        return res.values()
