import json 


json_open = open('../../input.json', 'r')
json_load = json.load(json_open)

Data = ["Data1" , "Data2"]
data = []


for i in Data:
    data.append(int(json_load[i]))
   
num1 = data[0]
num2 = data[1]
operation = json_load['type']


