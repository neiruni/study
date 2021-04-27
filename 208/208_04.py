
import json

json_open = open('read.json', 'r', encoding='utf-8')
json_load = json.load(json_open)


for i in json_load['program_list']:
    print(i['language'], i['type'], i['use'])
