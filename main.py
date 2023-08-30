word = input()
def reversed1(word):
    res = ''
    for i in range(len(word)-1,-1,-1):
        pass
rev = reversed1(word)
if word == rev:
    return True
else:
    return False