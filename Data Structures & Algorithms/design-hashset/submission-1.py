class linkedlist:
    def __init__(self,val = 0, pre = None, next = None):
        self.val = val
        self.pre = pre
        self.next = next

class MyHashSet:

    def __init__(self):
        self.arr = [linkedlist() for i in range(10000)]


    def add(self, key: int) -> None:
        if self.contains(key):
            return
        pos = key % 10000
        cur = self.arr[pos]
        while cur.next:
            cur = cur.next
        cur.next = linkedlist(key, cur)

    def remove(self, key: int) -> None:
        pos = key % 10000
        cur = self.arr[pos].next
        while cur:
            if cur.val == key:
                cur.pre.next = cur.next
                if cur.next:
                    cur.next.pre = cur.pre
                break
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        pos = key % 10000
        cur = self.arr[pos].next
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False