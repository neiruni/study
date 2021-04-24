import re


buf = input()

pattren1 = "[0-9]"


d = re.fullmatch(pattren1, buf)
print(d)


#if buf = :
