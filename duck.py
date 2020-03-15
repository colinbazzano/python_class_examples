# this is an example of association
class Bill():
    def __init__(self, description):
        self.description = description


class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(f"This duck has a {bill.description} and a {tail.length} tail.")


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
# This duck has a wide orange bill and a long tail.
