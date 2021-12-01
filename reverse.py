class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
    
    def reverse ( self ) :
        prev = None
        current = self.head
        while ( current is not None ) :
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

llist = LinkedList()
llist.head = Node ( 1 )
llist.head.next = Node ( 2 )
llist.head.next.next = Node ( 3 )
llist.reverse()
llist.printList()