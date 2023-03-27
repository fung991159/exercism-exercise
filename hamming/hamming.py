def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The length of two strand is different!")

    diff = sum([1 for l1, l2 in zip(strand_a, strand_b) if l1 != l2])
    return diff
