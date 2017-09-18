words_list = open('listado-general.txt')
words_content = words_list.read()
words = words_content.split()
vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
              'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


def w_vocal(le):
    # Is a vocal?
    v = False
    for k in vowels:
        if le == k:
            v = True
            break
    return v


def l_word_s(w):
    if len(w) >= 5:
        i = -1
        c = w_vocal(w[i])
        while c:
            try:
                yield w[i]
                i = i - 1
                c = w_vocal(w[i])
            except:
                break
        while not c:
            try:
                yield w[i]
                i = i - 1
                c = w_vocal(w[i])
            except:
                break
        try:
            yield w[i]
        except:
            pass
    else:
        for i in reversed(w):
            yield i


file = open('listas.txt', 'w')
for k in words:
    nk = ''.join(reversed(list(l_word_s(k))))
    file.write(nk)
    file.write("\n")