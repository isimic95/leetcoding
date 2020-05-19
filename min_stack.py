class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.currmin = 4294967296

    def push(self, x: (int)) -> None:
        self.currmin = min(x, self.currmin)
        self.l.append((x, self.currmin))

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        return self.l[-1][1]
