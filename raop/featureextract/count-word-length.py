import json

my_data = json.loads(open("C:\\tain1.json").read())

names = [item['request_text'] for item in my_data]

print json.dumps(names,indent =1)

for item in names:
    print len(item.split())



