def trychange(item):
    try:
        return int(item)
    except ValueError:
        return item


def frequency_sort(items):
    dict_items = {str(item): items.count(item) for item in items}
    ready = [[x] * y for x, y in dict_items.items()]

    A = [item for sublist in ready for item in sublist]

    B = []

    for x in A:
        B.append(trychange(x))
    return B


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")


