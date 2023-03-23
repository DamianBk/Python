"""Algorytm szybkiego sortowania quick sort"""


def divide(lst: list, start: int, end: int):
    i: int = start
    border_value: list = lst[end]

    for j in range(start, end):
        if lst[j] <= border_value:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[end] = lst[end], lst[i]

    return i


def quick_sort(lst: list, start: int, end: int):

    if start < end:
        border_index: int = divide(lst, start, end)
        quick_sort(lst, start, border_index - 1)
        quick_sort(lst, border_index + 1, end)


non_sorted = [20, 7, 5, 8, 33, 12, 334, 1, 3, 2, 8, 5, 9, 0]

quick_sort(non_sorted, 0, len(non_sorted) - 1)

print(non_sorted)
