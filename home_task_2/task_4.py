string = str(input('enter the word: '))
if string == string[::-1]:
    print(f'"{string}" is a Palindrome!')
else:
    print(f'"{string}" is not a Palindrome!')
    