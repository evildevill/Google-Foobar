from collections import defaultdict

def generate(c1, c2, bitlen):
    # Generate a new value by combining two input values bitwise
    a = c1 & ~(1 << bitlen)
    b = c2 & ~(1 << bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a & ~b & ~c & ~d) | (~a & b & ~c & ~d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d)

def build_map(n, nums):
    # Build a mapping of patterns based on the input numbers
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(1 << (n + 1)):
        for j in range(1 << (n + 1)):
            generation = generate(i, j, n)
            if generation in nums:
                mapping[(generation, i)].add(j)
    return mapping

def solution(g):
    g = list(zip(*g))  # Transpose the grid
    nrows = len(g)
    ncols = len(g[0])

    # Convert the grid cells into numbers
    nums = [sum([1 << i if col else 0 for i, col in enumerate(row)]) for row in g]
    mapping = build_map(ncols, nums)

    preimage = {i: 1 for i in range(1 << (ncols + 1))}
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())

    return ret
