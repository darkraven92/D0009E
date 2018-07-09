

class telefonbok:

    def __init__(self):
        self.teledict = {}
        self.kommandon = {"add":self.add}

    def menu(self):
        while True:
            x = input(print("> "))
            y = x.split()

    def add(self,namn,nummer):
        pass


if __name__ == "__main__":
    telefonbok().menu()