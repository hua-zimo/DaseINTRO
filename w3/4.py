class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
    
    def isempty(self):
        return self.head is None
    
    #增(尾部)
    def add(self, item):
        node = Node(item)
        if self.isempty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
    #删
    def remove(self, item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
                
    #查
    def find(self, item):
        return item in self.items()
    
    #改
    def update(self, item, value):
        if self.head:
            cur = self.head
            while cur is not None:
                if cur.item == item:
                    cur.item = value    