print("Вводите столько слов, сколько захотите. Когда Вы введете пустое слово, программа выдаст Вам нечто загадочное. Сможете понять закономерность?:)")
wordlist = []
while True:
	word = str(input("Введите слово: "))
	if len(word) == 0: 
		break
	else:
		wordlist += [word]
i = 1
for word in wordlist:
        if len(word) > 1:
                print(word[i:])
        else:
                print("")
        i += 1
