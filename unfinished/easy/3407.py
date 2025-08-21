def solution(s, p):
    first_part, second_part = p.split("*")
    index_s = 0
    index_p1 = 0
    index_p2 = 0
    while index_s < len(s):
        while index_p1 < len(first_part):
            if s[index_s] == first_part[index_p1]:
                index_p1 += 1
            index_s += 1


print(solution("leetcode", "ee*e"))