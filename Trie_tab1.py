import operator

n = int(input("Number of tasks: "))
m = int(input("Number of machines: ")) 
print("List of tasks:")
*tasks,=map(str,input().split())
print("List of periods:")
*periods,=map(float,input().split())

# n = 6
# m = 3
# tasks = ['A', 'B', 'C', 'D', 'E', 'F']
# periods = [10, 4, 1, 1, 2, 6.5]

dic = {}
for i in range(n):
    dic[tasks[i]] = periods[i]
dic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
duree = m * [0]
result = [[] for i in range(m)]

for task, period in dic.items():
    idxmin = duree.index(min(duree))
    result[idxmin].append(task)
    duree[idxmin] += period
print(result)
print(duree)