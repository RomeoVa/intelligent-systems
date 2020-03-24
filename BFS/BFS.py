'''

    BFS
 
    Mauricio Peón  A01024162
    Romeo Varela A01020736
    Germán Torres A01651423

'''

import csv
import numpy as np
with open('tree.csv', 'r') as file:
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
    #print(tree)

    for key,value in tree:
        dic_tree.setdefault(key, []).append(value)

    for key,value in tree:
        dicSonParent.setdefault(value, []).append(key)
    
    print("dicSonParent:")
    print(dicSonParent)

    for i in tree:
        for j in i:
            if j not in nodes:
                nodes.append(j) 
    dictionary = np.zeros((len(nodes),len(nodes)))

    for i in tree:
        dictionary[nodes.index(i[0])][nodes.index(i[1])] = 1
    for i,c in enumerate(dictionary):
        if sum(c) == 0:
            leafs.append(nodes[i])

    root = input('Enter the root: ') 
    goal = input('Enter the goal: ') 
    stack2 = []
    #print("ayayay: ",dictionary[nodes.index(root)])
    #stack.append(root) 
    path.append(root)
    for index, element in enumerate(dictionary[nodes.index(root)]):
        if element == 1:
                stack.append(nodes[index])
    #stack.pop()
    
    while stack:
        #print("stack", stack)
        stack2.append(stack.pop())
        #print("stack2", stack2)
        while stack2:
            i = stack2.pop()
            path.append(i)
            #stack2.append(nodes[i])
            for index, element in enumerate(dictionary[nodes.index(i)]):
                if element == 1:
                    stack2.append(nodes[index])
        
            #print("stack2: ",stack2)
            if goal in path:
                break
        if goal in path:
            break

        path = []
        path.append(root)

    key_list = list(dic_tree.keys()) 
    val_list = list(dic_tree.values()) 
    flag = 0
    #print(val_list)
    
    path = []
    while flag != None:
        path.append(goal)
        for index,lis in enumerate(val_list):
            if goal in lis:
                flag = index
                goal = key_list[flag]
                break
            else:
                flag = None
        #print("goal = ",goal,flag)
        
    #print(key_list[flag]) 

    print("path: ",path[::-1])
    
     
    print("Number of nodes: ", len(nodes))
    print("Number of leafs: ", len(leafs))
    print("Number of levels: ", len(dic_tree)+1)

def find(dicSonParent,path,currentNode):
    
    currentNode = dicSonParent[currentNode] 
    
    path.append(currentNode)

    if currentNode == None:
        return path

    return find(dicSonParent,path,currentNode)
