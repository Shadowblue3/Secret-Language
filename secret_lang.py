'''
Secret language rules:
    1-> if the string contains at least 3 characters then take the first character and append it at the end, then input any 3 random characters at the end and begin
    2-> else simply reverse it
'''
import string
import random

def convert_word(s):
    l1 = []
    temp = []
    for i in range(3):
        random_char = random.choice(string.ascii_letters)
        temp.append(random_char)
    for i in range(len(s)):
        l1.append(s[i])

    ch = l1.pop(0)
    l1.append(ch)

    for i in l1:
        temp.append(i)
    for i in range(3):
        random_char = random.choice(string.ascii_letters)
        temp.append(random_char)
    res = ''.join(temp)
    return res

def secret_lang(s):
    if(len(s) < 3):
        s = s[::-1]
        return s
    else:
        l = s.split()
        new_str = []
        for i in l:
            new_str.append(convert_word(i))
        result = ' '.join(new_str)
        print(result)

word = input("Enter a string: ")
secret_lang(word)
        
