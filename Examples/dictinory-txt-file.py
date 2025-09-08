file = open('file.txt')

def wdictionaryfin(file):
    newDictionary = dict()
    count = 0
    for line in file:
        word = line.strip()
        newDictionary[word] = count
        count = count + 1
    return newDictionary

x = wdictionaryfin(file)
print(x)

# {'My name': 0, 'is': 1, 'Mohammed': 2, 'Iftekhar': 3, 'I': 4, 'am': 5, 'in': 6, '6th semester': 7}
        