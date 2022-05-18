try:
    4/0
except ZeroDivisionError as e:
    print(e)

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()