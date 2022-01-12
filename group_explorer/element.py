import numpy as np
import cmath
import math

#Each element represents a complete graph on "nodes" nodes 
#with edges colored using "num_of_colors" colors.
class Element:
    #self.nodes = number of nodes in the graph
    #self.matrix = the nodes-1 x nodes-1 matrix representing the graph
    
    def __init__(self, nodes, num_of_colors, exponents):
        self.__nodes = nodes
        self.__num_of_colors = num_of_colors
        self.__matrix = np.zeros((nodes-1,nodes-1), dtype=complex)
        inc = 0
        pi = math.pi
        for i in range(nodes-1):
            for j in range(i, nodes-1):
                self.__matrix[i][j] = cmath.exp(complex(0, 2*exponents[inc]*pi/num_of_colors))
                inc += 1
                
    def __str__(self):
        return str(np.around(self.__matrix, decimals=2))
        
    def nodes():
        return self.__nodes
        
    def num_of_colors():
        return self.__num_of_colors
        
    def matrix():
        return self.__matrix
        
        
    def mult(elt, is_mat = False):
        if is_mat:
            return np.matmul(self.__matrix, elt)
        if (self.__nodes == elt.nodes() and 
            self.__num_of_colors == elt.num_of_colors()):   
            
            return np.matmul(self.__matrix, elt.matrix())
            
    
        