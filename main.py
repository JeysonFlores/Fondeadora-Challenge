def destructure(array: list) -> list:
    it = 0
    while it < len(array):
        if isinstance(array[it], list):
            if array[it]:
                array[it : (it + 1)] = destructure(array[it])
                it -= 1
            else:
                del array[it]
                it -= 1
        it += 1
    return array
