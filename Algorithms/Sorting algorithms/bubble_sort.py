"""Algorithm bubble sort"""


def bubble_sort(sequence: list):
    seq_len = len(sequence)

    for i in range(seq_len):
        for j in range(seq_len - 1):
            if sequence[i] < sequence[j]:
                sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence


unsorted = [2, 1, 3, 6, 4, 7, 5]

bubble_sort(unsorted)

print(unsorted)
