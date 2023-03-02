# https://leetcode.com/problems/valid-palindrome/
import re


def isPalindrome(s: str) -> bool:
    result = []

    for c in s:
        # 문자/숫자만 result에 (소문자로) 넣기
        if re.compile(r'\d|[a-zA-Z]').search(c):
            result.append(c.lower())

    # 왼쪽 절반과, 뒤집은 오른쪽 절반을 비교
    mid = len(result) // 2
    left = list(result[0:mid])
    right = list(result[(mid if len(result) % 2 == 0 else mid + 1):])
    right.reverse()

    # print(left)
    # print(right)

    return left == right


print(isPalindrome(s='race a car'))
print(isPalindrome(s="A man, a plan, a canal: Panama"))
print(isPalindrome(s=" "))