# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:56:47 2020

@author: rzava
"""

# Create Class Node:
class Node():
	def __init__(self, value = None, child = None):
		self.value = value
		self.child = child			

		
	def __str__(self):
		return str(self.value)


#Create LinkedList Class
class LinkedList():
    def __init__(self,value): ##setting root value to self
        self.head = value
        self.length = 0 #set length of list to 0, to be updated later
        
    def length(self): #super easy, return the variable we update
        return self.length
    
    def addNode(self, new_value): #must use ridiculous variable names
        noder = Node(value = new_value) #establish new node
        noded = self.head #make this the last value
        if self.head == None: #loop to update head if it is empty
            self.head = noder
        else:
            while noded.child != None:
                noded = noded.child
            noded.child = noder
        self.length += 1 #update length, so cool
        print(noder, "is linked to the end.  You're great.")   
        #confirmation/affirmation message     
        
    def addNodeAfter(self, new_value, after_node):
        noder = Node(value = new_value, child = after_node.child)
        #new node with no children 
        after_node.child = noder
        #establish parental relationsip
        self.length += 1
        print(str(self.length) + " is the new length of your list.  Congrats.")
        #confirmation/affirmation message     

    def addNodeBefore(self, new_value, before_node):
        noder = Node(value = new_value, child = before_node)
        noded = self.head
        #set last node to head
        #while loop to establish order
        while noded.child != noder:
            noder = noded.child
        noded.child = noder
        self.length += 1       
        print(str(self.length) + " is the new length of your list.  Congrats.")
        #confirmation/affirmation message     
        
#remove node using while loop to shift nodes into head until finding the right one    
    def removeNode(self, node_to_remove):
        noded = self.head
        while noded.child != node_to_remove:
            noded = noded.child
        noded.child = node_to_remove.child  
        self.length -= 1
        print(str(self.length) + " is the new length of your list.  Congrats.")
        #confirmation/affirmation message   
        
#similar concept        
    def removeNodesByValue(self, value):
        noded = self.head
        while (noded.child).value != value:
            noded = noded.child
        noded.child = noded.child.child  
        self.length -= 1
        print(str(self.length) + " is the new length of your list.  Congrats.")
        #confirmation/affirmation message   
        
    def reverse(self):
        noded = self.head
        prev = None
        latr = None
        while noded:
            latr = noded.child
            noded.child = prev
            prev = noded
            noded = latr
        self.head = prev
        
    def __str__(self):
        if self.head == None:   
            return "This is so empty."    
        # make sure we account for empty lists 
        else:
            #recursive statement to append our message with each item in the list
            print_me = ""
            noded = self.head
            while noded.child != None:
                print_me += str(noded.value) + "  ->  "
                noded = noded.child
            print_me += str(noded.value)      
            return f"Head = " + str(self.head.value) + ", \nTail = " + str(noded.value) + ", \nTotal list = " + str(print_me) + "."

#######        Testing        ########
            
UmListed = LinkedList(None)
print(UmListed)
## adding 7 nodes
UmListed.addNode(new_value = 10)
UmListed.addNode(new_value = 5)
UmListed.addNode(new_value = 28)
UmListed.addNode(new_value = 16)
UmListed.addNode(new_value = 2)
UmListed.addNode(new_value = 5)
UmListed.addNode(new_value = 80)
UmListed.length ## 7, rad
print(UmListed)

## Now flip it
UmListed.reverse() ## 
print(UmListed)
## yay 
## formally naming a node
ohNode = Node(235)
UmListed.head.child.child.child.child.child.child.child = ohNode
ohNode
print(UmListed)
##only to take it away
UmListed.removeNode(ohNode)
print(UmListed)
##woah
##Re-add it
UmListed.head.child.child.child.child.child.child.child = ohNode
UmListed.addNodeAfter(6, ohNode)
UmListed.addNodeBefore(555, ohNode)
print(UmListed)
##woooaaahhh
##but too many 5's
UmListed.removeNodesByValue(5)
print(UmListed)
##cool cool cool