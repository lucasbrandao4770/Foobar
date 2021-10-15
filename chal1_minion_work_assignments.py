test_cases = [
    ([1, 2, 3], 0),
    ([1, 2, 2, 3, 3, 3, 4, 5, 5], 1),
    ([], 1)
]


def solution(data, n):
    if n == 0:
        return []

    state = {}  # Dict holding the state of the variables
    for num in data:
        state[num] = 1 if num not in state else state[num] + 1

    data = [num for num in data if state[num] <= n]

    return data


def main():
    for t in test_cases:
        print(solution(t[0], t[1]))


if __name__ == "__main__":
    main()
