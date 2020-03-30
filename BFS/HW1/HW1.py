'''
    
    BFS - Search with weight an many parents

    Mauricio Peón  A01024162
    Romeo Varela A01020736
    Germán Torres A01651423

'''

import csv
import numpy as np

def findPaths(dicSonParent,finalPaths,path,cost,currentNode):
    
    parents = dicSonParent[currentNode]

    path = currentNode + path

    if parents[0][0] == None:
        finalPaths.append([path,cost])
        return

    for parent in parents:
        
        findPaths(dicSonParent,finalPaths,path,cost+int(parent[1]),parent[0])


with open('HW1.csv', 'r') as file:
    reader = csv.reader(file)
    tree  = []
    nodes = []
    leafs = []
    dictionary = []
    stack = []
    path = []
    dic_tree = {}
    dic_tree2 = {}
    dicSonParent = {}

    son = []
    levels = 1

    for row in reader:
        tree.append(row)
        #print(row)
    tree = tree[1:]

    dic_tree.setdefault('A', []).append([None,0])

    for key,value,value2 in tree:
        dic_tree.setdefault(value, []).append([key,value2])

    for item in dic_tree:
        print(repr(item),":",dic_tree[item])

    goal = input('Enter the goal: ')

    finalpaths = []
    findPaths(dic_tree,finalpaths,"",0,goal)

    print("paths",finalpaths)

    if len(finalpaths) > 0:
        minPath = finalpaths[0]
        maxPath = finalpaths[0]

    for path in finalpaths:
        if path[1] < minPath[1]:
            minPath = path
        
        if path[1] > maxPath[1]:
            maxPath = path

    print("Min path: ",minPath)
    print("Max path: ",maxPath)


