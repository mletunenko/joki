def is_merge(s, part1, part2):
    for i in s:
        pos = s.find(i)
        if pos >= 0:
            s = s[:pos] + s[pos+1:]
    if s == part2:
        return True
    return False



print(is_merge('sa', 's', 'a'))

