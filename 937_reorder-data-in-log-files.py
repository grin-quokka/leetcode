# https://leetcode.com/problems/reorder-data-in-log-files
def reorderLogFiles(logs):
    dig = []
    let = []

    # 문자 로그와 숫자 로그를 분리해서 저장한다
    for log in logs:
        if log.split(' ')[1].isdigit():
            dig.append(log)
        else:
            let.append(log)

    # 문자 로그 정렬 : 내용을 내림차순으로, 같으면 제목 숫자 기준으로
    let = sorted(let, key=lambda l: l.split(' ')[0])
    let = sorted(let, key=lambda l: l.split(' ')[1:])

    # 문자 로그, 숫자 로그 순으로 리턴
    return let + dig

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))
# Output: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]