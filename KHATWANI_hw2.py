'''
REFERENCES:
http://www.openbookproject.net/thinkcs/python/english2e/ch21.html
http://web.mit.edu/eranki/www/tutorials/search/
https://docs.python.org/3/reference/datamodel.html#object.__iter__

Name: MOHIT KHATWANI
Campus ID: AJ75499
HW2 - Part 2 - Path Finding

'''

import math

class Tree:
    count= 0
    '''
        Description of Nodes:
            A node contains following data:
                The value at that position in array
                position in which node is present
                g(n) : The cost from start node to present node
                h(n) : The cost from present node to Goal node
                f(n) = g(n) + h(n)
                left node, Right node
    '''
    def __init__(self,data,position,gval,hval,node_tag, left = None, right = None):
        self.count += 1
        self.data = data
        self.left = left
        self.right= right
        self.position = position
        self.hval = hval
        self.gval = gval
        self.fval = self.gval + self.hval
        self.node_tag = node_tag

    def __iter__(self):
        for i in range(self.count):
            return self
    def attach_left(self,node):
        self.left = node
    def attach_right(self,node):
        self.right = node
    def get_fval(self):
        return self.fval
    def get_tag(self):
        return self.node_tag
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right


def solve(problem):
    closed_list,open_list = [],[]
    start_index = 0
    found_solution = 0
    node_tag = ''
    if problem == []:
        return "No solution exists"
    root = Tree(problem[0],start_index,0,len(problem) - start_index,node_tag)
    gval = 0
    tempr = root
    open_list.append(tempr)
    while open_list != []:
        gval += 1
        #get minimum heuristic node from open list
        min_h = math.inf
        for n in open_list:
            h = n.get_fval()
            if h < min_h:
                node = n
        #checking if current node is goal before generating successor
        if node.position == (len(problem)-1):
            found_solution = 1
            break
        #remove the node from open list and append it in closed list while generating child nodes
        open_list.remove(node)
        #appending in closed list
        closed_list.append(node)
        #generation of child nodes
        #left operations
        if (node.position - problem[node.position]) > 0:
            check_presence = False
            left_node = Tree(problem[node.position - problem[node.position]],node.position - problem[node.position],gval,len(problem) - (node.position - problem[node.position]),node.get_tag()+'L')
            node.attach_left(left_node)
            for n in open_list + closed_list:
                if n.position == left_node.position:
                    check_presence = True   #To check whether left node is present in open list and closed list or not
            if not check_presence:
                open_list.append(left_node) # If not present then append it in open list

        #right operations
        if (node.position + problem[node.position]) < len(problem):
            check_presence = False
            right_node = Tree(problem[node.position + problem[node.position]], node.position + problem[node.position],gval, len(problem) - (node.position + problem[node.position]),node.get_tag() + 'R')
            node.attach_right(right_node)
            for n in open_list + closed_list:
                if n.position == right_node.position:
                    check_presence = True   #To check whether right node is present in open list and closed list or not
            if not check_presence:
                open_list.append(right_node)

    if found_solution:
        return node.get_tag()
    else:
        return "No solution exists"

if __name__ == "__main__":
    #q = [3,6,4,1,3,4,2,5,3,0]
    q = [1,1,1,1,1,1,1]
    print(solve(q))
