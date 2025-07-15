class LinkedListNode:
    def _init_(self,value,nextNode = None):
        self.value=value
        self.nextNode=nextNode

#creating objects
node1=LinkedListNode("1")
node2=LinkedListNode("2")
node3=LinkedListNode("3")
node4=LinkedListNode("4")
node5=LinkedListNode("5")
node6=LinkedListNode("6")
node7=LinkedListNode("7")
node8=LinkedListNode("8")

# linking the nodes
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8

currentNode = node1

while True:
    #dunno number of iterations u want to make:while loop
    #when u know the number of iterations you are to make:for loop

    print(currentNode.value,">>>",end=' ')

    if currentNode.nextNode is None:
        print("None")
        break

    currentNode = currentNode.nextNode
# ctrl + period/dot