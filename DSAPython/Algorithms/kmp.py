# KMP (Knuth-Morris-Pratt) algorithm is used to search for a pattern string in a text string in linear time.
def compute_lps(pattern):
    lps = [0] * len(pattern)
    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp(text, pattern):
    lps = compute_lps(pattern)
    i, j = 0, 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    return -1


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(kmp(text, pattern))  # Output: 10
