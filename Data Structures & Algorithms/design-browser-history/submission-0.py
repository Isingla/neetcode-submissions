class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.index += 1
        self.history = self.history[:self.index]
        self.history.append(url)

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.index > 0:
                self.index -= 1
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.index < len(self.history)-1:
                self.index += 1
        return self.history[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)