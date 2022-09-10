"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []  # a new list to copy elements into
    while i < len(x) or j < len(y):
        if i<len(x):
            z.append(x[0])
            x.pop(0)
        if j<len(y):
            z.append(y[0])
            y.pop(0)
    w=sorted(z)
    print(w)