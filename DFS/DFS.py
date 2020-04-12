'''
    
    DFS - Search

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


with open('DFS.csv', 'r') as file:
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
    to_Analyze = []
    visited = []
    parents = []

    for row in reader:
        tree.append(row)
        #print(row)
    tree = tree[1:]
    
    root = 'A'
    for key,value,value2 in tree:
        dic_tree.setdefault(key, []).append([value,value2])
        parents.append(key)
        if key not in nodes:
            nodes.append(key)
        if value not in nodes:
            nodes.append(value)
        
    for item in dic_tree:
        print(repr(item),":",dic_tree[item])

    #goal = input('Enter the goal: ')
    #print(sorted(nodes))

    to_Analyze.append('A')

    inGoal = False

    goal = input('Enter the goal: ')
    
    for element in dic_tree:
        dic_tree[element].sort(key = lambda x: x[1],reverse = True)
        #dic_tree[element].sort(reverse = True)
        print(element,dic_tree[element])

    while len(visited) != len(nodes) and inGoal == False:
        char = to_Analyze.pop()
        visited.append(char)

        if char in parents:
            for elements in dic_tree[char]:
                to_Analyze.append(elements[0])
        

        if char == goal:
            inGoal = True
        else:
            visited.pop()
        
        print("Analyze ",to_Analyze)
        
    
    print("path: ",visited)

    #print(sorted(dic_tree,key = lambda x: for x in dic_tree))
        
        
        

        
