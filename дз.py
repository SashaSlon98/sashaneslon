word = input("введите слово: ") 
for l in range(len(word)): 
    word = word[1:len(word)] + word[0]
    print(word)
