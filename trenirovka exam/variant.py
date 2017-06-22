import os
import re

def fun_1():
    f = open(r'text.xml', 'r', encoding="utf-8")
    l = 0
    ana = 0
    for r in f:
        if 'w' in r:
            l += 1
            ana += r.count('ana')
            
    print('Среднее количество разборов = {}'.format(ana/l))
    f.close()


def fun_2():
    f = open(r'text.xml', 'r', encoding="utf-8")
    
    d = {'S':0, 'A':0, 'NUM':0, 'ANUM':0, 'V':0, 'ADV':0, 'PREDIC':0,
         'PARENTH':0, 'SPRO':0, 'APRO':0, 'ADVPRO':0, 'PREDICPRO':0, 'PR':0,
         'CONJ':0, 'PART':0, 'INTJ':0}
    
    for r in f:
        if 'w' in r:
            for k in d.keys():
                if k in r:
                    d[k]+=1
    o = open('text_dict.txt', 'w')
    for k in d.keys():
        o.write('{}\t{}\n'.format(k, d[k]))
    print('Файл частотности создан и сохранен в папке, где хранится программа ')

    o.close()
    f.close()


def fun_3():
    f = open(r'text.xml', 'r', encoding="utf-8")
    q = 0
    text = []
    p = re.compile(r"[а-яёА-ЯЁ]+")
    for r in f:
        if 'w' in r:
            text.append(r)

    o = open('10.txt', 'w+')
    for r in text:
        if 'S' in r and 'ins' in r:
            for i in range(3, 0, -1):
                if q-i > 0:
                    o.write('{}{}'.format(p.search(text[q-i]).group(), text[q-i][text[q-i].index('</w>')+4:].replace('\n', '')))
            o.write('\t{}{}\t'.format(p.search(r).group(), r[r.index('</w>')+4:].replace('\n', '')))
            for i in range(1, 4):
                if q+i < len(text):
                    o.write('{}{}'.format(p.search(text[q+i]).group(), text[q+i][text[q+i].index('</w>')+4:].replace('\n', '')))
            o.write('\n')
        q += 1
    print('Файл со словами создан и сохранен в папке, где хранится программа')
        
def main():
    
    fun_1()

    fun_2()

    fun_3()

if __name__ == '__main__':
    main()
        
