import csv

def main():
    clues = {}
    with open('clues.csv', 'r', encoding='utf-8') as f:
        text = csv.reader(f, delimiter=',')
        for row in text:
           clues[row[0]] = row[1]
    n = 0
    keys = list(clues.keys())
    while n < len(clues):
        i = 0        
        while i <= len(keys[n]):
            if i < len(keys[n]):
                response = input(keys[n]+'...')
                if response == clues[keys[n]]:
                    print('Правильно!')
                    n += 1
                    break
                else:
                    print('Неправильно. У тебя ещё '+str(len(keys[n]) - i+1)+' попыток.')
                    i += 1
            else:
                print('У тебя закончились попытки. Правильный ответ: '+keys[n]+' '+clues[keys[n]])
                n += 1
            
if __name__ == '__main__':
    main()
