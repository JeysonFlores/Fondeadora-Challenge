def destructure(array: list) -> list:
    for index, el in enumerate(array):
        if isinstance(el, list):
            array[index : (index + 1)] = destructure(el)
    return array
