'''
    
    BFS - Search with weight an many parents

    Mauricio Peón  A01024162
    Romeo Varela A01020736
    Germán Torres A01651423

'''

import csv
import numpy as np

def findPath(dicSonParent,path,cost,currentNode):
    
    cost += int(dicSonParent[currentNode][0][1])

    currentNode = dicSonParent[currentNode][0][0]

    if currentNode == None:
        return {"path":path,"cost":cost}

    path.insert(0, currentNode)

    return findPath(dicSonParent,path,cost,currentNode)


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
    path = findPath(dic_tree,[goal],0,goal)

    print("Path:",path["path"])
    print("Cost:",path["cost"])


