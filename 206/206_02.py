

dict1 = {}
word = 'たったひとつのしんじつみぬく、みためはこども、ずのうはおとな'
word = list(word)

for i in word:
    if i in dict1.keys():
        dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1


for key, value in dict1.items():
    print(key, str(value) + '個')