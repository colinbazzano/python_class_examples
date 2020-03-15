class Parent:
    def __init__(self, name, wake_up):
        self.name = name
        self.wake_up = wake_up

    def present(self):
        print(f"{self.name} likes to wake up at {self.wake_up}")


class Child(Parent):
    def __init__(self, name, wake_up, fav_breakfast):
        super().__init__(name, wake_up)
        self.fav_breakfast = fav_breakfast

    def present(self):
        print(f"{self.name} likes to wake up at {self.wake_up} and is normally hungry for {self.fav_breakfast}")


roy = Parent("Roy", "6:30am")
tommy = Child("Tommy", "8:00am", "lucky charms")
jeff = Child("Jeff", "12:00pm", "Sausage Egg and Cheese on a bagel.")
roy.present()
tommy.present()
jeff.present()
