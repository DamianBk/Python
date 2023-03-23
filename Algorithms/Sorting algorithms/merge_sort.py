"""Sortowanie przez scalanie"""
from random import randint
from time import time


def sort_merge(lst: list):
    len_list = len(lst)
    sorted_list: list = []

    if len_list <= 1:
        sorted_list = lst
    else:
        middle_point = len_list // 2
        left_list: list = sort_merge(lst[:middle_point])  # type:ignore
        right_list: list = sort_merge(lst[middle_point:])  # type:ignore

        index_left = index_right = 0
        while index_left < len(left_list) and index_right < len(right_list):
            if left_list[index_left] < right_list[index_right]:
                sorted_list.append(left_list[index_left])
                index_left += 1
            else:
                sorted_list.append(right_list[index_right])
                index_right += 1

        sorted_list.extend(left_list[index_left:])
        sorted_list.extend(right_list[index_right:])

        # print(f'left: --> {left_list}  right: --> {right_list}')

    # print(f'Debug: {lst} --> {sorted_list}')
    return sorted_list


non_sorted: list = [randint(0, 10000) for x in range(10000)]


# start = time()
# sort_merge(non_sorted)
# end = time()

# print(f'Sorting duration for function sort_insert: {end - start}')

start = time()
sorted(non_sorted)
end = time()

print(f'Sorting duration for function sort_insert: {end - start}')



