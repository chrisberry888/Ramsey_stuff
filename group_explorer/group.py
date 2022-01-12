from element import *

class Group:
    
    
    def __init__(self, nodes, num_of_colors):
        size = int(nodes*(nodes-1)/2)
        exps = np.zeros(size)
        end = (num_of_colors-1) * np.ones(size)
        self.__nodes = nodes
        self.__num_of_colors = num_of_colors
        self.__identity = exps
        self.__elt_list = []
        while True:
            self.__elt_list.append(Element(nodes, num_of_colors, exps))
            if np.array_equal(exps, end):
                break
            exps[0] += 1
            for i in range(size):
                if exps[i] == num_of_colors:
                    exps[i] = 0
                    exps[i+1] += 1
                else:
                    break
            
            
    def __str__(self):
        return '\n\n'.join([str(elt) for elt in self.__elt_list])

    
    def get_list():
        return self.__elt_list
    