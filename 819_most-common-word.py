# https://leetcode.com/problems/most-common-word/
from collections import Counter
import re
import itertools
def mostCommonWord(paragraph, banned) :
    # 공백으로 단어 구분
    # 소문자로 바꾼 것을 알파벳 이외의 문자로 split 한다
    onlyWord = [re.split('[^a-z]', x.lower()) for x in paragraph.split()]

    # 이중배열을 풀어주고 중복 단어의 갯수를 카운트
    counter = Counter(itertools.chain(*onlyWord))

    # split 때문에 생긴 빈 문자열은 무시해야한다
    banned.append('')

    # 금지된 단어는 지워준다
    for b in banned:
        del counter[b]

    # 최빈 단어를 리턴한다
    return counter.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))
# Output: "ball"
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
# "b"


