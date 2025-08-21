def solution(s, p):
    first_part, second_part = p.split("*")
    if p == "*":
        return True
    index_s = 0
    first_bool = False
    second_bool = False
    print(len(second_part))
    if len(first_part) == 0:
        first_bool = True
    if len(second_part) == 0:
        second_bool = True
    while index_s < len(s) and first_bool:
        if s[index_s:index_s + len(first_part)] == first_part:
            first_bool = True
            index_s += (len(first_part) - 1)
        index_s += 1
    while index_s < len(s) and first_bool and second_bool:
        if s[index_s:index_s + len(second_part)] == second_part:
            second_bool = True
            index_s += (len(second_part) - 1)
        index_s += 1
    print(first_bool, second_bool)
    if first_bool and second_bool:
        return True
    return False


print(solution("leetcode", "*ee"))