import sys



fl = open('wiki.txt', 'r')
words = fl.read()
freq = words.split()


##for line in fl.readlines():
##    line = line.strip('\n')
##    (f, w) = line.split('\t')
##    freq.append((int(f), w))

text = "Houston Hoston is awesome"
text1 = text.split()
for words in text1:
    if words in freq:
        print (words, end=' ')
    else:
        print(words+'*', end=' ')


