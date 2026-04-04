class ll():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Deque:
    
    def __init__(self):
        self.left = ll(0, None, None)
        self.right = ll(0, self.left, None)
        self.left.right = self.right

    def isEmpty(self) -> bool:
        if self.left.right == self.right:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        new = ll(value)
        cur = self.right.left
        cur.right = new
        new.left = cur
        new.right = self.right
        self.right.left = new


    def appendleft(self, value: int) -> None:
        new = ll(value)
        nxt = self.left.right
        self.left.right = new
        new.left = self.left
        nxt.left = new
        new.right = nxt


    def pop(self) -> int:
        if self.left.right == self.right:
            return -1
        lastval = self.right.left
        lastsec = lastval.left
        lastsec.right = self.right
        self.right.left = lastsec
        return lastval.val

    def popleft(self) -> int:
        if self.left.right == self.right:
            return -1
        firstval = self.left.right
        secval = firstval.right
        self.left.right = secval
        secval.left = self.left
        return firstval.val

