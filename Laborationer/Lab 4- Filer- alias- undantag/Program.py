class telefonbok:

    def __init__(self):
        self.teledict = {}
        kommandon_dict = {"add":self.add, "lookup": self.lookup}

    while True:

        x = input("> ")
        y = x.split()

    def add(self, namn, nummer):
        self.teledict[nummer] = namn
        print(namn,":",nummer,"är tillagt")

    def lookup(self, namn):
        for numb, na in self.teledict.items():
            if namn in na:
                print(numb)
            else:
                print("Namnet hittades inte")







t = telefonbok()