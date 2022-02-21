# Дополнительно (рекурсивно):
# https://leetcode.com/problems/reverse-string/
# Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["h","e","l","l","o"]


def count_down(i):
    a = []
    if len(i) == 1:
        a.extend(i[:1])
    else:
        a.extend(i[-1]) # последний
        a.extend(count_down(i[:-1])) # без последнего
    return a


b = count_down(s)
print(b)

