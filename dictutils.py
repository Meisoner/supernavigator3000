def keydictsearch(dct, wrd):
    res = []
    if type(dct) == dict:
        for i in dct.keys():
            if wrd.lower() in i.lower():
                res += [dct[i]]
            res += keydictsearch(dct[i], wrd)
    elif type(dct) == list:
        for i in dct:
            res += keydictsearch(i, wrd)
    return res


def valdictsearch(dct, wrd):
    res = []
    if type(dct) == dict:
        vals = dct.values()
    else:
        vals = dct
    for i in vals:
        if type(i) == str:
            if wrd.lower() in i.lower():
                res += [i]
        else:
            res += valdictsearch(i, wrd)
    return res