
# Linked Lists

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next  # go to the adress of the next place in the memory [pointer]
        
def print_list(head):
    h = head
    while h is not None:
        print(h.value)
        h = h.next

def AddNode(head, value):
    node = ListNode(value)
    if head is None:
        head = node
    else:
        h = head
        while h.next != None:
            h = h.next
        h.next = node
    return head

def AddNode_with_index(head, value, index):
    node = ListNode(value)
    if head is None:
        head = node
    elif index == 0:
        node.next = head
        head = node
    else:
        h = head
        i = 0
        while i < index and h.next != None:
            h = h.next
            i += 1
        node.next = h.next
        h.next = node
    return head

def get_element(head, index):
    h = head
    i = 0
    while i < index and h != None:
        h = h.next
        i += 1
    if h != None:
        print(h.value)
    else:
        raise ValueError('Index out of range')


def remove_element(head, value):
    h = head
    q = None  # create a new node set right before the head
    while h != None and h.value != value:
        q = h
        h = h.next
    if h == None:
        print('Element not found')
    else:
        if h == head:
            """ move the head to the next node ignoring the first one [ignore the first element - remove first element] """ 
            head = head.next  
        else:
            """  move the pointer of the previous node to the next of the current node 
            [ignore the current node - remove current element some where in the middle] """
            q.next = h.next
    return head


# 6 << 7 << 8     [ctrl + k + c] to comment and [ctrl + k + u] to uncomment

node1 = ListNode(6)
node2 = ListNode(7)
node3 = ListNode(8)

node1.next = node2
node2.next = node3
head = node1

print(head.value)
print_list(head)
head = AddNode(head, 9)
print_list(head)

# 6 << 7 << 8 << 9
get_element(head, -3)
get_element(head, 3)

print_list(head)
head = remove_element(head, 7)
print_list(head)


