import random


def shuffle_list(input):
    first = input[0]
    others = []
    for item in input:
        if item != first:
            others.append(item)
    random.shuffle(others)
    result = others[0:3]
    result.append(first)
    random.shuffle(result)
    return result


