# https://leetcode.com/problems/encode-and-decode-strings/ (facebook)
# https://www.youtube.com/watch?v=B1k_sxOSgv8&ab_channel=NeetCode

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Example :: ["neetco#de"] -> encoded_string -> 4#neet5#co#de -> decoded_string = "neetco#de"

'''
Documentation
  pick a delimiter : #. But what if # already present (sami#t mohan) -> sami t mohan (instead of samit mohan)
  need 2 delimiter -> len of string and #
  neet, co#de -> 4#neet, 5co#de
  always going to be an integer (len) before the string followed by delimiter (#) -> read 4 letters after # and remove delimiter.

Time Complexity :  O(N) -> N = total number of characters
'''

'''
@param: strs: a list of strings
@return: encodes a list of strings to a single string
'''


def encode(strs):
    res = ""
    for s in strs:
        # encode
        res += str(len(s)) + "#" + s  # 4#neet
    return res


'''
@param: str: A string
@return: decodes a single string to a list of strings
'''


def decode(str):
    # 4#neet5#co#d
    res, i = [], 0  # i = what posn am i at in the input string
    while i < len(str):  # read every char
        j = i
        while str[j] != "#":  # still at integer
            j += 1  # until we get to pound character
        # how many following char we have to read after len (neet) : 4
        length = int(str[i:j])
        # j = n(neetcode)
        res.append(str[j + 1: j + 1 + length])  # gives us entire string (neet)
        # start at next work (update pointer i)
        i = j + 1 + length  # neet done, 5#co#de left

    return res


def main():
    encode_string = ["neet", "co#de"]
    decode_string = "4#neet5#co#de"

    print(encode(encode_string))  # -> 4#neet5#co#de
    print(decode(decode_string))  # -> ['neet', 'co#de']


main()
