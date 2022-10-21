def insertion_sort(element, list):
    # inserts an element and automatically sorts it in the list
    if list == []:
        return list
    swaps = False
    if not swaps:
        list.append(element)
        for j in range(len(list)):
            for i in range(len(list) - 1 - j):
                if list[i] < list[i + 1]:
                    temp = list[i + 1]
                    list[i + 1] = list[i]
                    list[i] = temp
                    swaps = True


def noves_fora(list):
    if len(list) == 0: return list

    steps = [list + []]
    nine_out = 0
    for i in range(len(list)-1):
        if len(list) >= 2:
            nine_out = list[0] + list[1]
            if nine_out >= 9:
                nine_out = nine_out - 9
            list.pop(0)
            list.pop(0)
        if len(list) != 0:
            insertion_sort(nine_out, list)
            steps.append(list + [])
    list.append(nine_out)
    steps.append(list + [])

    return list[0], steps
