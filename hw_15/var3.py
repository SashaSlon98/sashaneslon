import re
b = input ('Название статьи: ')
f = open(b, 'r', encoding = 'utf-8')
q = input ('Новая статья: ')
l = open(p, 'w', encoding = 'utf-8')

m = f.readlines()
for elmnt in m:
    elmnt = re.split(' ', elmnt)
    elString = ""
    for word in elmnt:
        word = re.sub(u'язык', u'шашлык', word)
        word = re.sub(u'Язык', u'Шашлык', word)
        elString += word + ' '
    elmnt = elString
    print(elmnt)
    h.write(elmnt)
