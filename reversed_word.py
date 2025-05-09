'''reversed word '''
def reverse_words(text):
    te = text.split(" ")
    s = []
    for n in te :
        r = []
        for l in n :
            r.append(l)
        r.reverse()
        r =''.join(r)
        s.append(r)
    return ' '.join(s)
print(reverse_words('ahmed'))