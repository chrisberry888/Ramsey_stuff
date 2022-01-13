from element import *
from group import *

#Group(x,y) means K_x with the edges y-colored

def start():
    nodes = 3
    num_col = 2
    my_group = Group(nodes, num_col)
    
    ident = my_group.get_identity()
    for i in range(len(my_group)):
        curr = my_group[i]
        lst = []
        for j in range(len(my_group)):
            lst.append(curr.mult(my_group[j]))
            
        #if len(lst) == len(set(lst)):
        #    print("No dups")
        #else:
        #    print("Doesn't work")
        for elt in lst:
            print(elt)
            print()
        print()
        print()
        print()
    
    
    
    
start()