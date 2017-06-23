# файл с новостями необходимо разархивировать и поместить в общую папку вместе с данной программой

import os


def fun_5():
    path = '{}\\news'.format(os.getcwd())
    cout = 0
    for f in os.listdir(path):
        o = open('{}\\{}'.format(path, f), 'r+')
        for line in o:
            if 'w' in line:
                cout += 1
        sf = open('slova.txt', 'a+')
        sf.write('{}\t{}\n'.format(f, cout))
        cout = 0

def fun_8():
    path = '{}\\news'.format(os.getcwd())
    sv = open('table.csv', 'a+')
    sv.write('Название файла,Автор,Дата создания текста\n')
    for f in os.listdir(path):
        o = open('{}\\{}'.format(path, f), 'r+')
        sv.write('{},'.format(f))
        for line in o:
            if 'author' in line:
                sv.write('{},'.format(line[line.index('=')+1:line.index('name')].replace('"', '').strip()))
            if 'created' in line:
                sv.write('{}\n'.format(line[line.index('=')+1:line.index('name')].replace('"', '').strip()))
        

    
def main():
    fun_5()
    print('Файл с количеством слов создан и сохранен в папке, где хранятся новости и эта программа ')
    fun_8()
    print('Файл с таблицей создан и сохранен там же')

if __name__ == '__main__':
    main()
