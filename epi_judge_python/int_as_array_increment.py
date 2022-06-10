from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # brute force method
    # b = int("".join(map(str, A)))
    # arr = []
    # for c in str(b + 1):
    #     arr.append(int(c))
    # return arr

    # indices method
    e = len(A) - 1
    b_e = len(A) - 2
    A[-1] += 1

    while b_e >= 0:
        if A[e] == 10:
            A[e] = 0
            A[b_e] += 1
            e -= 1
            b_e -= 1

        else:
            e -= 1
            b_e -= 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    # if A[0] == 10:
    #     A[0] = 0
    #     A.insert(0, 1)

    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
