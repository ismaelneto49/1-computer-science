def maximum(list):
    # returns the biggest value in the given list
    if list != []:
        biggest = list[0]
        for e in list:
            if e > biggest:
                biggest = e
        return biggest


def minimum(list):
    # returns the smallest value in the given list
    if list != []:
        smallest = list[0]
        for e in list:
            if e < smallest:
                smallest = e
        return smallest


def index(element, list):
    # returns the index of the given element in the list
    if contains(element, list):
        index = 0
        for i in range(len(list)):
            if list[i] == element:
                index = i
                return index


def last_index(element, list):
    # returns the last index of the given element in the list
    if contains(element, list):
        negative_index = -1
        for i in range(-1, ((len(list)+1) * -1), -1):
            if list[i] == element:
                negative_index = i
                index = len(list) + negative_index
                return index


def insert(element, position, list):
    # inserts the given element in the given position of the list
    if list == []:
        list.append(element)
        return list
    list.append(list[-1])
    for i in range(len(list)-1, position, -1):
        list[i] = list[i-1]
    list[position] = element
    return list


def remove(element, list):
    # removes the given element of the list
    if contains(element, list):
        list.pop(index(element, list))
        return list
    return list


def insertion_sort(element, list):
    # inserts an element and automatically sorts it in the list
    if list == []:
        return list
    swaps = False
    if not swaps:
        list.append(element)
        for j in range(len(list)):
            for i in range(len(list) - 1 - j):
                if list[i] > list[i + 1]:
                    temp = list[i + 1]
                    list[i + 1] = list[i]
                    list[i] = temp
                    swaps = True
    return list


def sort(list):
    # sorts the given list
    if list == []:
        return list
    swaps = False
    if not swaps:
        for j in range(len(list)):
            for i in range(len(list) - 1 - j):
                if list[i] > list[i + 1]:
                    temp = list[i + 1]
                    list[i + 1] = list[i]
                    list[i] = temp
                    swaps = True
    return list


def alpha_sort(sequence):
    # sorts the given sequence alphabetically
    if sequence == '':
        return sequence

    sequence_list = []
    for e in sequence:
        sequence_list.append(e)
    sequence_list.sort()
    final_sequence = f''
    for i in sequence_list:
        final_sequence += i
    return final_sequence


def slice(start, end, list):
    # returns a sublist of the given list
    if list == []:
        return list
    sliced = []
    for i in range(start, end):
        sliced.append(list[i])
    return sliced


def replace(target, element, list, all=True):
    # replace `all` occurences of the target in the list with the given element
    if contains(target, list):
        if all:
            for i in range(len(list)):
                if list[i] == target:
                    list[i] = element
            return list
        else:
            for i in range(len(list)):
                if list[i] == target:
                    list[i] = element
                    break
            return list
    return list


def contains(element, list):
    # returns a boolean representing if the element is or is not present in the given list
    for e in list:
        if e == element:
            return True
    return False
