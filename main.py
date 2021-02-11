import sys
import itertools
string = ''
k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(0, m):
    muchie = sys.stdin.readline().split()
    nod1 = int(muchie[0])
    nod2 = int(muchie[1])
    graph[nod1 - 1][nod2 - 1] = 1
    graph[nod2 - 1][nod1 - 1] = 1
#print(graph)
literals = []
for i in range(1, n*k + 1):
    literals.append(i)
# print(literals)
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] == 1:
            string += '('
            for x in range(0, k):
                string += str(literals[i * k - x + (k - 1)]) + 'V' + str(literals[j * k - x + (k - 1)]) + 'V'
            string = string[:-1]
            string += ')^'
            graph[i][j] = -1
            graph[j][i] = -1

for x in range(0, k):
    tat = []
    #string += '('
    for i in range(0, len(literals), k):
        tat.append(literals[i - x])
        #string += str(literals[i - x]) + 'V'
    #string = string[:-1]
    #string += ')^'
    c = list(itertools.combinations(tat, 2))
    #print(c)
    for i in c:
        string += '(~'
        for j in range(2):
            string += str(i[j]) + 'V~'
        string = string[:-2]
        string += ')^'
for i in range(0, n*k, k):
    string += '(~'
    for j in range(k):
        string += str(literals[i + j]) + 'V~'
    string = string[:-2]
    string += ')^'
string = string[:-1]
print(string)
