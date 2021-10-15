import itertools

test_cases = [
    ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
    ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
    ["1"]
]


def to_string(ver):
    ver = [str(item) for item in ver if item is not None]
    ver = '.'.join(ver)
    return ver


def make_tuple(ver):
    # Transforms the strings into a uniformized tuple
    ver = ver.split('.')
    ver = [int(item) for item in ver]
    while len(ver) < 3:
        ver.append(None)

    return tuple(ver)


def is_bigger(t1, t2):
    # Returns True if t1 is bigger than t2
    is_true = False
    for n1, n2 in itertools.izip(t1, t2):
        if n1 > n2:
            is_true = True
            break
        elif n1 < n2:
            break

    return is_true


def solution(l):
    # Separates the strings based on sublevels
    l = [make_tuple(item) for item in l]

    # Bubblesort
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if is_bigger(l[j], l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]

    # Transforming back to string
    l = [to_string(item) for item in l]

    return l


def main():
    for item in test_cases:
        print solution(item)


if __name__ == "__main__":
    main()
