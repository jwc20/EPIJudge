from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    res = [[1]]

    if n == 0:
        return []

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        # print(res)
        print(temp)
        for j in range(len(res[-1]) + 1):

            print(temp[j], temp[j+1])
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res


print(generate_pascal_triangle(5))

"""
if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
    """
