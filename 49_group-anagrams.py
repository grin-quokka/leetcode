import collections
def groupAnagrams(strs) :
    dic = {}
    print(collections.defaultdict(list))
    for s in strs:
        # 내림차순을 key로 설정
        key = ''.join(sorted(s))
        if key in dic:
            dic[key].append(s)
        else:
            dic[key] = [s]

    # print(dic)
    # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

    # 밸류만 모아서 리턴
    return list(dic.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# [["bat"],["nat","tan"],["ate","eat","tea"]]