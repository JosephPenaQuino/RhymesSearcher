words_list = open('listado-general.txt')
words_content = words_list.read()
words = words_content.split()

rhymes_list = open('listas.txt')
rhymes_content = rhymes_list.read()
rhymes = rhymes_content.split()

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
    i = -1
    c = w_vocal(w[i])
    while c:
        yield w[i]
        i = i - 1
        c = w_vocal(w[i])
    while not c:
        yield w[i]
        i = i - 1
        c = w_vocal(w[i])
    yield w[i]


ans = []
s_word = input("Enter a spanish word: ")
k = ''.join(reversed(list(l_word_s(s_word))))
for index, e in enumerate(rhymes):
    if e == k:
        print(words[index])
