def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        # swap
        s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


reverseString(["h", "e", "l", "l", "o"])
# ["o","l","l","e","h"]
