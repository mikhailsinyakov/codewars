def flatten(*args):
    def flatten_list(elements):
        for el in elements:
            if type(el) == list:
                yield from flatten_list(el)
            else:
                yield el

    return list(flatten_list(args))
