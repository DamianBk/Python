def sort_select(sequence: list):

    for run in range(len(sequence)):
        min_ind = run
        for i in range(run + 1, len(sequence)):
            if sequence[i] < sequence[min_ind]:
                min_ind = i
        sequence[run], sequence[min_ind] = sequence[min_ind], sequence[run]


unsorted = [1, 6, 5, 3, 0, 9, 8, 11, 3, 2]

sort_select(unsorted)

print(unsorted)
