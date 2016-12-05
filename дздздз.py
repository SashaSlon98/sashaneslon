
count1 = 0 
count3 = 0 

with open('download-excel (2).txt','r') as f: 
    for line in f: 
        for word in line.split(): 
            if len(word) == 3: 
                count3 = count3 + 1 
            if len(word) == 1: 
                count1 = count1 + 1 
if count1 == 0 :
    print('Dough') 
count3 = count3/count1 
print('Слов из 3х букв больше слов из 1 буквы в столько раз')
print(count3)
