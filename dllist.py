class _Node:
    def __init__(self, prevNode, nextNode, element):
        self.__prev = prevNode
        self.__next = nextNode
        self.__element = element


    def get(self):
        return self.__element

    def prev(self):
        return self.__prev

    def next(self):
        return self.__next

    def setPrev(self, node):
        self.__prev = node

    def setNext(self, node):
        self.__next = node

class _Sentinel(_Node):
    def __init__(self):
        super().__init__(None, None, None)
    
class DoubleLinkedList:
    def __init__(self):
        self.__header = _Sentinel()
        self.__trailer = _Sentinel()
        self.__header.setNext(self.__trailer)
        self.__trailer.setPrev(self.__header)

    def isEmpty(self):
        # return isinstance(self.__header.next(), _Sentinel)
        return self.__header.next() == self.__trailer

    def addFront(self, element):
        node = _Node(self.__header, self.__header.next(), element)
        node.prev().setNext(node)
        node.next().setPrev(node)
        return self

    def addBack(self, element):
        node = _Node(self.__trailer.prev(), self.__trailer, element)
        node.prev().setNext(node)
        node.next().setPrev(node)
        return self

    def front(self):
        # if self.isEmpty():
        #     return None
        return self.__header.next().get()
    
    def back(self):
        return self.__trailer.prev().get()

    def removeFront(self):
        nodetoBeDeleted = self.__header.next()
        nodetoBeDeleted.next().setPrev(nodetoBeDeleted.prev())
        nodetoBeDeleted.prev().setNext(nodetoBeDeleted.next())
        return nodetoBeDeleted.get()