def is_pal_perm(s):
    s = s.lower()
    s = s.replace(" ","")

    d = dict()

    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    
    odd_count = 0
    print(d)

    for v in d.values():
        if v%2 == 1 and odd_count == 0:
            odd_count += 1
        elif v%2 == 1 and odd_count > 0:
            return False
    return True


s = "tacotaaac"

print(is_pal_perm(s))