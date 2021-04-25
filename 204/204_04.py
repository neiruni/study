import re


buf = input()

pattren1 = "[0-9]+"
pattren2 = "[0-9a-zA-Z]+"
pattren3 = "[0-9a-zA-Z\.\ \']+"
pattren4 = "[0-9]+-[0-9]+-[0-9]+"


one = re.fullmatch(pattren1, buf)
two = re.fullmatch(pattren2, buf)
three = re.fullmatch(pattren3, buf)
four = re.fullmatch(pattren4, buf)


if one is not None:
    print('The character strings are all half-width numbers.')
elif two is not None:
    print('The character strings are all alphanumeric characters.')
elif three is not None:
    print('The character string is half-width English.')
elif four is not None:
    print('The string is a phone number.')
else:
    print('The string is neither.')
