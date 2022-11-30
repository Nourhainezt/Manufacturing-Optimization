# Manufacturing-Optimization
#The first file (Sort_tab) allows to sort the data table and to display the result (List of tasks assigned to the three machines). The second file(Affichage_diag) #allows to display the Gantt chart using the graphic library Plotly.
#NB: complexité: O(n*m).


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
#Diagramme de Gantt
import plotly
import plotly.figure_factory as ff
diag=[dict(Task=tasks[0],Start='2021-02-12 : 0', Finish= '2021-02-12: '+ str(result[0]) ),
      dict(Task=tasks[1],Start='2021-02-12: '+ str(result[0]), Finish= '2021-02-12: '+ str(result[1]) ,
      dict(Task=tasks[2],Start='2021-02-12: '+ str(result[1]), Finish= '2021-02-12: '+ str(result[2]) ),
      
fig=ff.create_gantt(diag)
plotly.offline.plot(fig, filename='gantt.html')
