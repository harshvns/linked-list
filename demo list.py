class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node({0})".format(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def addLast(self, data):
        newnode = Node(data)
        newnode.next = None
        if self.head is None:
            self.head = newnode
            return
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = newnode

    def traverse(self):
        head = self.head
        print()
        while head is not None:
            print(head, end=",")
            head = head.next
        print()

    def __len__(self):
        head = self.head
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return length

    def search(self, data):
        head = self.head
        while head is not None:
            if head.data == data:
                return True
            head = head.next
        return False

    def delete(self, data):
        temp = self.head
        if temp is None:
            return
        if temp.data == data:
            temp.head = temp.next
            return
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next
        return

    def reverse(self):
        if self.head is None:  # 0 node
            return
        p = self.head
        if p.next is None:  # 1 node
            return
        q = p.next
        if q.next is None:  # 2 node
            self.head = q
            q.next = p
            p.next = None
            return
        r = q.next  # at least 3 nodes
        while r.next is not None:
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p
        self.head.next = None
        self.head = r
        r.next = q

    def mid(self):

        if self.head is None:
            return None
        p = self.head
        if p.next is None:
            return None

        q = p.next
        if q.next is None:
            return p
        p = self.head
        q = p.next
        while True:
            p = p.next
            q = q.next
            if q is None:
                return p
            q = q.next
            if q is None:
                return p

        # p=self.head
        # f=self.head
        # while f is not None:
        #     p = p.next
        #     f=p.next.next
        #     if f==None:
        #         return p


a = LinkedList()
for i in range(1, 12):
    a.addLast(i)
a.traverse()
midnode = a.mid()
if midnode is None:
    print(midnode)
else:
    print(midnode.data)
