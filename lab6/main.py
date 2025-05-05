def hash_func(string) -> int:
    hash = 0
    alphabet = len(set(string))
    for i in range(len(string)):
        sym = string[i]
        hash += (ord(sym) * (alphabet ** i)) % 100
    return hash

def rabin_karp(text, pattern) -> int:
    pl = len(pattern)
    pttr_hs = hash_func(pattern)
    for i in range(len(text) - pl):
        if hash_func(text[i:i + pl]) == pttr_hs:
            print('!!!')
            if text[i:i + pl] == pattern:
                return i
    return -1


if __name__ == '__main__':
    text = 'aaa bbc cabbca ac'
    pattern = 'c ca'
    rk = rabin_karp(text, pattern)
    if rk == -1:
        print('substr not found')
    else:
        print(rk)
