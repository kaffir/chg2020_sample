class Node(object):
    def __init__(self, letter,frequency,left,right):
        self.letter = letter
        self.left = left
        self.right = right
        self.frequency = frequency

#Parse dictionary or map as a parameter 
#   {alphabet(char) : frequency (int)}
#return a tree (root node)
def generateTree(letter_dict): 
    #** Only Use THIS algorithm to generate a tree, otherwise your final result may be incorrect!
    Node_list=[]

    #iterate to each charactor in dictionary
    #create a node for each charactor including alphabet(char) and frequency
    #*APPEND* all nodes to Node_list (insert to the end of the list)
    for i in letter_dict:
        if (letter_dict[i] != 0):
            Node_list.append(Node(i,letter_dict[i],None,None))

    #pop 2 nodes as node1,node2 that has *SMALLEST FREQUENCY* from the list
    #Create a new node that has the previous 2 node as a left and right child
    #Set frequency of the new node = node1.frequency + node2.frequency
    #***node1 MUST be the left child and node2 MUST be the right child***(node1.frequency <= node2.frequency)
    #insert the new node back *IN FRONT OF* the list
    #Repeat... until the list contains only 1 node (root node)
    #return the root node
    while(len(Node_list)>1): 
        temp_node1 = Node_list.pop(Node_list.index(min(Node_list,key = lambda node:node.frequency)))
        temp_node2 = Node_list.pop(Node_list.index(min(Node_list,key = lambda node:node.frequency)))
        Node_list.insert(len(Node_list),Node(None,temp_node1.frequency+
            temp_node2.frequency,temp_node1,temp_node2))
    return Node_list[0]

#Example
frequency_example = {'b':5,'o':7,'a':9,'t':2}

#the function will return a root node that contains all nodes (whole tree)
#you can examine root by using IDE debugger
root = generateTree(frequency_example)
exit()

    #     O
    #    / \
    #   a   o
    #      / \
    #     o   o   
    #        / \
    #       t   b
