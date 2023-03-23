"""Algorithm merge sort"""


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

    return sorted_list
