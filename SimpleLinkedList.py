class Node:
    def _init_(self,data):
        #constructor : initializes and declares variables and attributes
        self.data=data

        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None


    def insertAtTheBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def printList(self):
        temp = self.head

        while temp:
            print(f"{temp.data} ", end='')
            temp = temp.next

        print()


if __name__=='main_':
    llist = LinkedList()

    llist.insertAtTheBeginning("New")
    llist.insertAtTheBeginning("Data")
    llist.insertAtTheBeginning("Is")
    llist.insertAtTheBeginning("New")
    llist.insertAtTheBeginning("Data") #the last one runs first

    llist.printList()