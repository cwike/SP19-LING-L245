import sys



fl = open('wiki2.txt', 'r')
words = fl.read()
freq = words.split()

text = str(input("Enter a String: "))
text1 = text.split()
for words in text1:
    if words in freq:
        print (words, end=' ')
    else:
        print(words+'*', end=' ')


