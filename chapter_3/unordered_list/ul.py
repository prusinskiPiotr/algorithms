class Node:
    # It is always a good idea to explicitly assign None to your initial next reference values.
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
    

class UnorderedList:

    # unordered list will be built from a collection of nodes, 
    # each linked to the next by explicit references
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current != None:
            previous = current
            current = current.getNext()

        previous.setNext(temp)

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 1
        temp = Node(item)
        while current != pos:
            count = count + 1
            previous = current
            current = current.getNext()
        
        previous.setNext(temp)

    def index(self, item):
        current = self.head
        index = 0
        while current != item:
            index = index + 1
            current = current.getNext()
        return index

    def pop(self, pos):
        current = self.head
        count = 0
        while count != pos
            count = count +1
            current = current.getNext()
        return remove(current)



        

    