def maximum(array):
    # returns the biggest value in the given array
    if array == [] or array == [None]:
        return None
    biggest = array[0]
    for e in array:
        if e > biggest:
            biggest = e
    return biggest


def minimum(array):
    # returns the smallest value in the given array
    if array == [] or array == [None]:
        return None
    smallest = array[0]
    for e in array:
        if e < smallest:
            smallest = e
    return smallest


def index(element, array):
    # returns the index of the given element in the array
    if contains(element, array):
        index = 0
        for i in range(len(array)):
            if array[i] == element:
                index = i
                return index


def last_index(element, array):
    # returns the last index of the given element in the array
    if contains(element, array):
        negative_index = -1
        for i in range(-1, ((len(array)+1) * -1), -1):
            if array[i] == element:
                negative_index = i
                index = len(array) + negative_index
                return index


def insert(element, position, array):
    # inserts the given element in the given position of the array
    if array == [None]:
        array[0] = element
        return array

    for i in range(len(array)-1, position, -1):
        array[i] = array[i - 1]
    array[position] = element
    return array


def remove(element, array):
    # removes the given element of the array
    if contains(element, array):
        for i in range(index(element, array), len(array)-1):
            array[i] = array[i + 1]
        array[-1] = None
        return array
    return array


def insertion_sort(element, array):
    # inserts an element and automatically sorts it in the array
    if array == []:
        return array
    swaps = False
    if not swaps:
        array[-1] = element
        for j in range(len(array)):
            for i in range(len(array) - 1 - j):
                if array[i] > array[i + 1]:
                    temp = array[i + 1]
                    array[i + 1] = array[i]
                    array[i] = temp
                    swaps = True
    return array


def sort(array):
    # sorts the given array
    if array == [] or array == [None]:
        return array
    swaps = False
    if not swaps:
        for j in range(len(array)):
            for i in range(len(array) - 1 - j):
                temp = 0
                if array[i] > array[i + 1]:
                    temp = array[i + 1]
                    array[i + 1] = array[i]
                    array[i] = temp
                    swaps = True
    return array


def slice(start, end, array):
    # returns a subarray of the given array
    if array == [None] or array == []:
        return array
    index = 0
    sliced = (end - start) * [None]
    for i in range(start, end):
        sliced[index] = array[i]
        index += 1
    return sliced


def replace(target, element, array, all=True):
    # replace `all` occurences of the target in the array with the given element
    if contains(target, array):
        if all:
            for i in range(len(array)):
                if array[i] == target:
                    array[i] = element
            return array
        else:
            for i in range(len(array)):
                if array[i] == target:
                    array[i] = element
                    break
            return array
    return array


def contains(element, array):
    # returns a boolean representing if the element is or is not present in the given array
    for e in array:
        if e == element:
            return True
    return False
