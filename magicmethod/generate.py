

def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            print nested
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                # yield element
                pass
    except TypeError:
        print nested
        # yield nested

flatten([1,2, 3,])
# for f in flatten([[1, [2, 3]], 4, [5, 6]]):
#     print f

