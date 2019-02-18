import sys

lineCounter  = 0
tokenCounter = 0
charCounter = 0 

for char in sys.stdin.read():
	if char == '\n':
		lineCounter = lineCounter + 1
	if char == ' ':
		tokenCounter = tokenCounter + 1
	#if char == char:
	charCounter = charCounter + 1
		
		
	   
print('Lines:')
print(lineCounter)
print(" ")
print('Tokens:')
print(tokenCounter)
print(" ")
print('Char:')
print(charCounter)