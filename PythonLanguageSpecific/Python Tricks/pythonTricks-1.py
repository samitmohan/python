"""
1. Bisect
2. sortedcontainers
3. lru_cache
4. defaultdict
5. setrecursionlimit
"""

# Bisect module : bisect_left and bisect_right. Both functions take a sorted list and a search value as input,
# and return the index where the value would be inserted in the list to maintain its sorted order.
# bisect_left : returns index of leftmost occurrence f target
# bisect_right : returns index of rightmost occurrence of target

import bisect
from functools import lru_cache

from sortedcontainers import SortedList


def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)  # leftmost occurrence
    if index < len(arr) and arr[index] == target:
        return index
    return -1


arr = [1, 2, 3, 4, 5]
target = 3
ans = binary_search(arr, target)
if ans:
    print(f"{target} found at index {ans}")
else:
    print("Not found")

# sortedcontainers : provide efficient sorted list / dict / set data types.
# performs insertion lookups deletions in O(log(n)) [faster than built in O(n) list type]

lst = SortedList()
lst.add(3)
lst.add(1)
lst.add(2)
print(lst)  # [1, 2, 3]
lst += [4, 6, 5]
lst.remove(4)
print(lst)  # [1, 2, 3, 5, 6]
print(lst)  # [1, 2, 3, 4, 5, 6]

# lru_cache :  decorator that allows you to cache the results of a function and improve its performance.

# works by storing the results in a cache, with the input values as the key and the output values as the value
# when function called again lru_cache decorator retrieves the output values from the cache instead of re-executing.

"""Parameters -: You can specify the maximum size of the cache using the maxsize parameter. When the cache reaches 
its maximum size, the lru_cache decorator discards the least recently used entries to make room for new ones.

The lru_cache decorator stores the results of the function in a cache and retrieves them from the cache instead of 
re-executing the function, greatly improving its performance.
"""


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(40))  # easily calculated

# defaultdict : convenient way to work with dictionaries that have a default value for keys that do not exist.
# Benefits : eliminates the need to check whether a key exists before accessing or updating its value

from collections import defaultdict

# Create a defaultdict with a default value of 0
word_count = defaultdict(int)
strings = ["apple", "banana", "apple", "cherry", "banana"]

# Count the frequency of each word
for word in strings:
    word_count[word] += 1

# Print the word count
print(word_count)  # defaultdict(int, {'apple': 2, 'banana': 2, 'cherry': 1})

# setrecursionlimit : function to increase the maximum recursion depth:
# function to increase the maximum recursion depth:

import sys

# Increase the maximum recursion depth to 5000
sys.setrecursionlimit(5000)


def recursive_function(n):
    if n > 0:
        return recursive_function(n - 1)
    else:
        return 0


# Call the recursive function 5000 times
print(recursive_function(5000))  # 0
