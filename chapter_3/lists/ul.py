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
        self.tail = None

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

    def index(self, item):
        current = self.head
        count = 0
        try:
            while current.getData() != item:
                count = count + 1
                current = current.getNext()
            else:
                return count
        except AttributeError:
            return None

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        temp = Node(item)
        while count is not pos and current is not None:
            previous = current
            current = current.getNext()
            count = count + 1
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def pop(self, pos=None):
        if pos == None:
            pos = self.size() - 1
        current = self.head
        previous = None
        count = 0
        while count is not pos:
            previous = current
            current = current.getNext()
            count = count + 1
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getData()



mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))
# print(mylist.remove(93))
print(mylist.insert(0, 22))
print(mylist.index(22))
print(mylist.search(22))
# print(mylist.index(1))
print(mylist.size())
print(mylist.pop())
print(mylist.pop(1))
print(mylist.size())
# print(mylist.index(31))

        

    
