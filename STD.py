import csv
import math
with open("data.csv" , newline= "") as f:
     reader = csv.reader(f)
     file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total=0
    for i in data:
        total += int(i)
    mean = total/n
    return mean

squared_list = []

for number in data:
    a = int(number) - mean(data)
    a = a*2
    squared_list.append(a)

sum = 0

for num in squared_list:
    sum +=num 

result = sum/(len(data)-1)

std_dev = math.sqrt(result)

print(f"this is the result :  {std_dev}")


