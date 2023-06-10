def clamp(value, minimum, maximum):
    if value > minimum:
        return value if value < maximum else maximum
    return minimum


def dot_product(v1, v2):
    v1l = len(v1)
    assert v1l == len(v2)
    s = 0
    for i in range(0, v1l):
        s += v1[i] * v2[i]
    return s


def smoothstep(x):
    return 6 * pow(x, 5) - 15 * pow(x, 4) + 10 * pow(x, 3)


def lerp(v1, v2, t):
    return v1 + t * (v2 - v1)


def merge(l1, l2, join):
    if not isinstance(l1, (list, tuple)):
        return join(l1, l2)
    l = len(l1)
    assert l == len(l2)
    l3 = []
    for e in range(l):
        l3.append(merge(l1[e], l2[e], join))
    return l3
