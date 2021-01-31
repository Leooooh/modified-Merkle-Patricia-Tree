def raw_to_hex(string):
    assert isinstance(string, str), "Input must be string!"
    _hex = []
    for s in string:
        _hex += divmod(ord(s), 16)
    return _hex

def hex_to_raw(a):
    assert len(a) % 2 == 0
    result = ""
    for i in range(0, len(a), 2):
        result += chr(16 * a[i] + a[i + 1])

    return result

def hex_to_hp(a):
    if a[-1] == 16:
        term = 1
        a = a[:-1]
    else:
        term = 0
    oddlen = len(a) % 2
    flag = 2*term+oddlen
    
    if not oddlen:
        a = [flag, 0] + a
    else:
        a = [flag] + a
    result = ''
    for i in range(0, len(a), 2):
        result += chr(16 * a[i] + a[i + 1])
    return result

def hp_to_hex(nib):
    res = raw_to_hex(nib)
    flag = res[0]
    if flag & 2:
        res.append(16)
    if flag & 1:
        res = res[1:]
    else:
        res = res[2:]
    return res
    
def ter(nib, has_ter):
    if has_ter:
        nib.append(16)
    else:
        if nib[-1] == 16:
            del nib[-1]
    return nib

