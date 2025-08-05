

class sll:

    def __init__(self,value,next=None):

        self.value = value 
        self.next = next 
    
    def __str__(self):
        return str(self.value)



head = sll(45)
a = sll(57)
b = sll(89)
c = sll(44)
d = sll(90)


head.next = a
a.next = b 
b.next = c
c.next = d


def displayAllNode(head):

    current = head

    holder = []

    while current:
        holder.append(str(current.value))

        current = current.next 

    print(' --> '.join(holder))



def searchNode(head,value):

    current = head

    while current: 


        if value == current.value:
            return True 
        
        current = current.next 

    return False 


def removeMiddleOnly(head,node_value):

    current = head

    while current and current.next:
        if current.next.value == node_value:
            current.next = current.next.next 
            break
        
        current = current.next 
    
    return head

print("before : ")
displayAllNode(head)




removeMiddleOnly(head,57)

print("after : ")


displayAllNode(head)

print(searchNode(head,57)) 
