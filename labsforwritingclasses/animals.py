from abc import abstractmethod
class Bird:
    def __init__(self, can_fly):
        self.can_fly = can_fly
    @abstractmethod
    def fly():
        pass
class Owl(Bird):
    def __init__(self):
        super().__init__(can_fly=True)
    def fly(self):
        print("Maybe if you ask more nicely")
class Dodo(Bird):
    def __init__(self):
        super().__init__(can_fly=False)
    def fly(self):
        print("I am too extinct to do that")
dodo=Dodo()
dodo.fly()
owl=Owl()
owl.fly()
