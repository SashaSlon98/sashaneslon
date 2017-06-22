import os

arrAbc = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd'
          , 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

swith = 0 
kFolder = 0
path = os.getcwd()

for i in range (len(os.listdir(path))):
    if os.path.isdir(os.listdir(path)[i]):
        for x in range (len(os.listdir(path)[i])):
            if os.listdir(path)[i][x] in arrAbc:
                swith = 1
        if swith == 0:
            kFolder +=1
        swith = 0
        
print("Папок с киррилическими символами: ", kFolder, "\n")
print("Список файлов: ")

file = []
status = 0

for i in range (len(os.listdir(path))):
    name = os.listdir(path)[i]
    if os.path.isfile(name):
        filename, file_ext = os.path.splitext(name)
        for x in range(len(file)):
            filename1, file_ext1 = os.path.splitext(file[x])
            if filename == filename1:
                status = 1
        if status == 0:
            file.append(name)
        status = 0
    else:
        if name not in file:
            file.append(name)

for i in range (len(file)):
    print(file[i])

