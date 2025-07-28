'''
@author: Yogeshwar Shukla 
@date: 26th April 2025 
@goal: To implement singly linked list of integers 
'''

def generic_exception_handler(trace=False): 
    from sys import exc_info 
    excName, excData, excTb = exc_info() 
    print(excName, excData, sep=':', flush=True)
    if trace is True: 
        from traceback import print_tb 
        print_tb(excTb) 

class SNode: 
    '''
    This class implements a node for singly linked list and 
    singly circular linked list 
    '''

    def __init__(self, init_data: int): 
        '''
        @input: 
            @init_data: integer to be stored in a newly allocated node
        Constructor creates two attribtes in a newly allocated node 
        viz. i) 'data' : initialized by local variable 'init_data' 
        ii) 'next' : initialized to None. This is a self reference 
        to the next in sequence node in a collection 
        '''
        #print('----Entered SNode.__init__()----')
        if type(init_data) != int and init_data is not None: 
            raise TypeError(f'{init_data} is not of type int')
        self.data = init_data 
        self.next = None 
        #print(f'SNode.__init__():self.__dict__:{self.__dict__}')
        #print('----Leaving SNode.__init__()----')


class SinglyCircularLinkedList: 
    '''
    This class implements singly linked list ADT. 
    '''
    def __init__(self): 
        '''
        An attribute named 'head_node' will be created in a newly allocated 
        object of class SinglyLinkedList. The attribute name will be assigned 
        to a newly allocated dummy node object of class SNode. (Note that 
        the dummy node is the one whose 'data' attribute is None)
        '''
        #print('----Entered SinglyLinkedList.__init__()----')
        self.headNode = SNode(None)
        self.headNode.next = self.headNode #CHANGE 1 
        #print(f'SinglyLinkedList.__init__():self.__dict__:{self.__dict__}')
        #print('----Leaving SinglyLinkedList.__init__()----')

    def insertStart(self, newData: int): 
        '''
        @input: 
            @newData: new data to be insert at the starting position of the linked list
        newData will be encapsulated in a new SNode object and the newly allocated SNode 
        object will be positioned at the beginning after the linked list (immediately 
        next to the head node)
        '''
        #print('----Entered SinglyLinkedList.insertStart()----')
        if type(newData) != int: 
            raise TypeError(f'{newData} is not of the type int')
        # LOGIC 
        newNode = SNode(newData)
        newNode.next = self.headNode.next
        self.headNode.next = newNode
        #print('----Leaving SinglyLinkedList.insertStart()----')

    def insertEnd(self, newData: int): 
        #print('----Entered SinglyLinkedList.insertEnd()----')
        if type(newData) != int: 
            raise TypeError(f'{newData} is not of the type int')
        run = self.headNode 
        while run.next is not self.headNode: # CHANGE 2 None -> self.headNode 
            run = run.next 
        newNode = SNode(newData) # Change 3 run.next to newNode 
        newNode.next = self.headNode # Change 4 
        run.next = newNode # Change 5 
        #print('----Leaving SinglyLinkedList.insertEnd()----')

    def showList(self): 
        '''
        Display the data members of all nodes except the head node 
        '''
        print('[START]->', end='')
        run = self.headNode.next 
        while run is not self.headNode: # Change 6  
            print(f'[{run.data}]->', end='')
            run = run.next 
        print('[END]')

    def searchNode(self, searchData: int): 
        '''
        @input: 
            @searchData: data value to be searched. 
        returns the node containing first occurrence of search_data
        and the node previous to it. 
        returns None if the searchData is not present. 
        '''
        #print('----Entered SinglyLinkedList.searchNode()----')
        run = self.headNode.next 
        runPrev = self.headNode
        while run is not None: 
            if run.data == searchData: 
                return (run, runPrev)
            runPrev = run
            run = run.next 
        #print('----Leaving SinglyLinkedList.searchNode()----')
        return (None, None)
    

    def insertAfter(self, existingData: int, newData: int): 
        '''
        @input: 
            @existingData: Datavalue which is supposed to be present in the list. 
            @newData: Data value that must be inserted after the first occurrence 
                of the @existingData. 
        a) Inserts a newly allocated node containing @newData after the node 
        containing the first occurrence of existingData. 
        b) raise ValueError if existingData is not found. 
        '''
        #print('----Entered SinglyLinkedList.insertAfter()----')
        existingNode, _ = self.searchNode(existingData)
        if existingNode is None: 
            raise ValueError(f'SinglyLinkedList.insertAfter():existingData:{existingData } not found')
        newNode = SNode(newData)
        newNode.next = existingNode.next 
        existingNode.next = newNode 
        #print('----Leaving SinglyLinkedList.insertAfter()----')

    
    def insertBefore(self, existingData: int, newData: int): 
        '''
        @input: 
            @existingData: Datavalue which is supposed to be present in the list. 
            @newData: Data value that must be inserted before the first occurrence 
                of the @existingData. 
        a) Inserts a newly allocated node containing @newData before the node 
        containing the first occurrence of existingData. 
        b) raise ValueError if existingData is not found. 
        '''
        #print('----Entered SinglyLinkedList.insertBefore()----')
        existingNode, existingNodePrev = self.searchNode(existingData)
        if existingNode is None: 
            raise ValueError(f'SinglyLinkedList.insertAfter():existingData:{existingData } not found')
        newNode = SNode(newData)
        existingNodePrev.next = newNode 
        newNode.next = existingNode
        #print('----Leaving SinglyLinkedList.insertBefore()----')

    
    def getStart(self) -> int: 
        '''
        a) Returns data value in the first node with data without removing the first node. 
        b) raise ValueError if the list is empty 
        '''
        #print('----Entered SinglyLinkedList.getStart()----')
        if self.headNode.next is None: 
            raise ValueError('getStart() cannot be applied on empty list')
        #print('----Leaving SinglyLinkedList.getStart()----')
        return self.headNode.next.data
    

    def getEnd(self) -> int: 
        '''
        a) Returns data value in the last node with data without removing the last node. 
        b) raise ValueError if the list is empty 
        '''
        #print('----Entered SinglyLinkedList.getEnd()----')
        if self.headNode.next is None: 
            raise ValueError('getEnd() cannot be applied on empty list')
        run = self.headNode 
        while run.next is not None: 
            run = run.next 
        #print('----Leaving SinglyLinkedList.getEnd()----')
        return run.data 


    def popStart(self) -> int: 
        '''
        a) Remove the first node with data and return the data value int it
        b) raise ValueError if the list is empty 
        '''
        #print('----Entered SinglyLinkedList.popStart()----')
        if self.headNode.next is None: 
            raise ValueError('popStart() cannot be applied on empty list')
        fisrtNodeWithData = self.headNode.next 
        firstData = fisrtNodeWithData.data
        self.headNode.next = fisrtNodeWithData.next
        del fisrtNodeWithData 
        #print('----Leaving SinglyLinkedList.popStart()----')
        return firstData 

    def popEnd(self) -> int: 
        '''
        a) Remove the last node with data and return the data value int it
        b) raise ValueError if the list is empty 
        '''
        #print('----Entered SinglyLinkedList.popEnd()----')
        if self.headNode.next is None: 
            raise ValueError('popEnd() cannot be applied on empty list')
        runPrev = self.headNode 
        run = self.headNode.next 
        while run.next is not None: 
            runPrev = run 
            run = run.next
        lastData = run.data
        runPrev.next = None 
        del run 
        #print('----Leaving SinglyLinkedList.popEnd()----')
        return lastData 

    def removeStart(self): 
        '''
        a) Removes the first node with data in the list. 
        b) raise ValueError if the list is empty 
        '''
        #print('----Entered SinglyLinkedList.removeStart()----')
        if self.headNode.next is None: 
            raise ValueError('removeStart() cannot be applied on empty list')
        fisrtNodeWithData = self.headNode.next 
        self.headNode.next = fisrtNodeWithData.next
        del fisrtNodeWithData 
        #print('----Leaving SinglyLinkedList.removeStart()----')

    def removeEnd(self): 
        '''
        a) Removes the last node with data in the list 
        b) raise ValueError if the list empty 
        '''
        #print('----Entered SinglyLinkedList.removeEnd()----')
        if self.headNode.next is None: 
            raise ValueError('removeEnd() cannot be applied on empty list')
        runPrev = self.headNode 
        run = self.headNode.next 
        while run.next is not None: 
            runPrev = run 
            run = run.next
        runPrev.next = None 
        del run 
        #print('----Leaving SinglyLinkedList.removeEnd()----')

    def removeData(self, rData: int): 
        '''
        @input: 
            @rData: Data value whose first occurrence within linked list must be removed
        Remove the first node containing value @rData 
        raise ValueError if the @rData does not exist
        '''
        #print('----Entered SinglyLinkedList.removeData()----')
        rNode, rNodePrev = self.searchNode(rData)
        if rNode is None: 
            raise ValueError(f'Data to be removed {rData} does not exist in the list')
        rNodePrev.next = rNode.next 
        del rNode 
        #print('----Leaving SinglyLinkedList.removeData()----')

    
    def find(self, fData: int) -> bool: 
        '''
        @input: 
            @fData: data value to be searched in list
        '''
        #print('----Entered SinglyLinkedList.find()----')
        existingNode, _ = self.searchNode(fData) 
        #print('----Leaving SinglyLinkedList.find()----')
        return existingNode is not None 


    def length(self) -> int: 
        '''
        Returns number of data nodes in the calling linked list 
        '''
        #print('----Entered SinglyLinkedList.length()----')
        counter = 0 
        run = self.headNode.next 
        while run is not None: 
            counter += 1 
            run = run.next 
        #print('----Leaving SinglyLinkedList.length()----')
        return counter 

    
    def isEmpty(self) -> bool: 
        '''
        Returns whether or not the calling list object is empty
        ''' 
        #print('----Entered SinglyLinkedList.isEmpty()----')
        #print('----Leaving SinglyLinkedList.isEmpty()----')
        return self.headNode.next is None 
    
    
    def concat(self, other): 
        newList = SinglyCircularLinkedList() 
        lastNode = newList.headNode 
        run = self.headNode.next 
        while run is not self.headNode: 
            newNode = SNode(run.data)
            lastNode.next = newNode 
            lastNode = lastNode.next 
            run = run.next 
        run = other.headNode.next 
        while run is not other.headNode: 
            newNode = SNode(run.data)
            lastNode.next = newNode 
            lastNode = lastNode.next 
            run = run.next 
        lastNode.next = self.headNode 
        other.headNode.next = None 
        del other.headNode 
        del other 
        return newList 

    def append(self, other): 
        pass 

    
    def merge(self, other): 
        pass 


    def getReversedList(self): 
        pass 

    
    def reverse(self): 
        pass 

# Client Side 
# Create a new object of class SinglyLinkedList for testing purpose 
print('----------------Creating a new SinglyLinkedList object-----------------')
L = SinglyCircularLinkedList() 
print('----------------Testing for empty list----------------')
try: 
    data = L.getStart() 
except: 
    generic_exception_handler() 

try: 
    data = L.getEnd() 
except: 
    generic_exception_handler() 

try: 
    data = L.popStart() 
except: 
    generic_exception_handler() 

try: 
    data = L.popEnd() 
except: 
    generic_exception_handler() 

try: 
    data = L.removeStart() 
except: 
    generic_exception_handler() 

try: 
    data = L.removeEnd() 
except: 
    generic_exception_handler() 

n = L.length() 
print(f'Length of empty list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print('----------------Testing insertStart()----------------')
for data in range(1, 6): 
    L.insertStart(data * 10) 

print('Showing list after L.insertStart():')
L.showList() 

print('----------------Testing insertEnd()----------------')
for data in range(6, 11): 
    L.insertEnd(data * 10)

print('Showing list after L.insertEnd():')
L.showList() 

print('----------------Testing insertAfter() for non-existent data----------------')
try: 
    L.insertAfter(-50, 1000)
except: 
    generic_exception_handler()

print('----------------Testing insertAfter() for middle node----------------')
L.insertAfter(10, 500)
L.showList() 

print("----------------Testing insertAfter() for the last node(boundary condition testing)----------------")
L.insertAfter(100, 1000)
L.showList() 

print('----------------Testing insertBefore() for non-existent data----------------')
try: 
    L.insertBefore(-50, 1000)
except: 
    generic_exception_handler()

print('----------------Testing insertBefore() for middle node----------------')
L.insertBefore(10, 600)
L.showList() 

print("----------------Testing insertBefore() for the first node(boundary condition testing)----------------")
L.insertBefore(50, 5000)
L.showList() 

print('----------------Testing getStart(), getEnd() on non-empty list----------------')
firstData = L.getStart() 
lastData = L.getEnd() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.getStart() and L.getEnd() to prove that start and end nodes are not removed")
L.showList()

print('----------------Testing popStart(), popEnd() on non-empty list----------------')
firstData = L.popStart() 
lastData = L.popEnd() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.popStart() and L.popEnd() to prove that start and end nodes are removed")
L.showList()

print('----------------Testing removeStart() and removeEnd() on non-empty list----------------')
L.removeStart() 
L.showList() 
L.removeEnd() 
L.showList() 

print('----------------Testing removeData() for non-existing data value----------------')
try:
    L.removeData(-400)
except: 
    generic_exception_handler() 

print('----------------Testing removeData() for the middle data----------------')
L.removeData(60)
L.showList() 

print('----------------Testing removeData() for the first node (boundary condition testing)----------------')
L.removeData(L.getStart())
L.showList() 

print('----------------Testing removeData() for the last node(boundary condition testing)----------------')
L.removeData(L.getEnd())
L.showList()

print('----------------Testing length()/isEmpty() on non-empty list----------------')
n = L.length() 
print(f'Length of list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print('----------------END----------------')

