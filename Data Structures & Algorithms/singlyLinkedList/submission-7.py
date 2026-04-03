class ll:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next 
class LinkedList:
    
    def __init__(self):
        self.dummy = ll()

    
    def get(self, index: int) -> int:
        cur = self.dummy.next
        for i in range(index):
            if not cur:
                return -1
            cur = cur.next
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        self.dummy.next = ll(val, self.dummy.next)

    def insertTail(self, val: int) -> None:
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = ll(val)

    def remove(self, index: int) -> bool:
        cur = self.dummy
        while cur and index:
            index -= 1
            cur = cur.next
        if not cur or not cur.next:
            return False
        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.dummy.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res