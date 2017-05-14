import os

path = os.getcwd()
file = []
ext = []
cout_ext = []
count = 0
two_cext = []

for root, dirs, files in os.walk(path):
    for name in files:
        file.append(name)
        filename, file_ext = os.path.splitext(name)
        if file_ext not in ext:
            ext.append(file_ext)

for i in range(len(ext)):
    cout_ext.append(0)

for i in range(len(ext)):
    for j in range(len(file)):
        filename, file_ext = os.path.splitext(file[j])
        if file_ext == ext[i]:
            count += 1
    cout_ext[i] = count
    count = 0

two_cext = cout_ext.copy()
cout_ext.sort(reverse=True)

for i in range(len(cout_ext)):
    index = two_cext.index(cout_ext[i])
    print("*", ext[index], " - ", two_cext[index])
    ext.pop(index)
    two_cext.pop(index)
