"""algorithm insertion sort"""


def insert_sort(sequence: list):
    for index in range(1, len(sequence)):
        current_index = index - 1
        next_value = sequence[current_index + 1]

        while sequence[current_index] > next_value and current_index >= 0:
            sequence[current_index + 1] = sequence[current_index]
            current_index = current_index - 1

        sequence[current_index + 1] = next_value


unsorted = [1, 4, 5, 3, 0, 2, 10, 6, 8, 7, 11, 9]

insert_sort(unsorted)

print(unsorted)
