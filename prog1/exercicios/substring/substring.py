def is_substring(s1, s2):

    # List of all sequencial substrings of the size of s2
    list_subs = []

    # Quantity of substrings of the size of s2
    iterations = (len(s1) - len(s2)) + 1
    for i in range(iterations):
        subs = ''
        for j in range(i, len(s2) + i): # CHURRAS: 0,  7 + 0; HURRASC: 1, 7 + 1
            subs = f'{subs}{s1[j]}'
        list_subs.append(subs)
    
    # Verifying if s2 is one of the sequencial substrings
    for s in list_subs:
        if s == s2:
            return True
    return False
