from django.test import TestCase

# Create your tests here.



import  json

b = {1:['a', 'b', 'c'], 2:['b', 'c', 'd'], 3:['a', 'c', 'd']}

b = json.dumps(b)

b = json.loads(b)

new_dic = {}

for i, k in b.items():
    for v in k:
        if v not in new_dic:
            new_dic[v] = []
            new_dic[v].append(i)

        else:
            new_dic[v].append(i)

print new_dic