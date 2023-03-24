def destructure(array: list) -> list:
    scoped_stack = []

    for el in array:
        if isinstance(el, list):
            scoped_stack.extend(destructure(el))
        else:
            scoped_stack.append(el)

    return scoped_stack


data = [1, [2, [3, [4, 5]]]]

print(destructure(data))