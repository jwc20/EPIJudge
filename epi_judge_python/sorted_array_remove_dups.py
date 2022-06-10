import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        print(
            "i: ",
            i,
            ", wi: ",
            write_index,
            ", A[write_index - 1]: ",
            A[write_index - 1],
            ", A[i]: ",
            A[i],

        )
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


delete_duplicates([2,3,5,5,7,11,11,11,13])


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
        """
