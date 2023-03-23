"""Algorithm bubble sort"""


def bubble_sort(sequence: list):
    seq_len = len(sequence)

    for i in range(seq_len):
        for j in range(seq_len - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence


unsorted = [0, 1, 9, 3, 6, 4, 7, 5]

bubble_sort(unsorted)

print(unsorted)
