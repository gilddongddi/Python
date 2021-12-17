#13강 종프_실습3_데이터분석


import csv
import matplotlib.pyplot as plt

f=open('2002.csv')
data=csv.reader(f)
header=next(data)
print(header)

temp=[]
for row in data:
    temp.append(row[1])

temp=list(map(float, temp))
print(temp)

plt.title('Average temperature graph')
plt.plot(temp, linewidth=5)
plt.xlabel('day')
plt.ylabel('temperature')



f.close() 
