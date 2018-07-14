class TelefonBok:
    def __init__(self):
        self.teleDic = {}
        kommandonDic = {"add": self.add, "lookup": self.lookup,
                    "alias": self.alias, "save": self.save,
                    "load": self.load, "remove": self.remove, "quit": self.my_quit, "change": self.change}

        while True:
            x = input("telefonbok> ")
            y = x.split()
            try:
                kommandonDic[y[0]](*y[1:])
            except KeyError:
                print("Denna funktion finns inte")
            except TypeError:
                print("du skriver fel antal argument")
            except SystemExit:
                print("Avslutar...")
                break


    def find(self, namn):
        hittade = 0
        nr = 0
        for number, names in self.teleDic.items():
            if namn in names:
                nr = number
                hittade += 1
        if hittade == 0:
            return 0
        elif hittade == 1:
            return nr
        else:
            return -1


    def add(self, namn, nummer):
        print("Namn:",namn,"\nNummer:",nummer,"\nSparat i telefonboken")
        self.teleDic[nummer] = [namn]


    def lookup(self, namn = None):
        if namn == None:
            print("Ge ett namn!")
        else:
            hittade = 0 #Hittade är 0 från början
            for number, names in self.teleDic.items():
                if namn in names:
                    print("Namn",namn,"\nNummer:",number)
                    hittade = 1
                    print("Done...")
            if hittade != 1:
                print("Namnet finns inte")

    def alias(self, namn, newname):
        if newname:
            nr = self.find(namn)
            if nr > 0: #om nr är större än 0...
                self.teleDic[nr].append(newname)
                print("Alias angivet...")


    def change(self, namn, newnumber, oldnr = None):
        if namn:
            nr = self.find(namn)
            if nr > 0: #om nr är större en 0.
                self.teleDic[newnumber] = self.teleDic[nr]
                del self.teleDic[nr]
                print("Namn ändrat...")
            elif nr == 0:
                print("Hittar inga med det nummer")
            else:
                if oldnr:
                    self.teleDic[newnumber] = self.teleDic[oldnr]
                    del self.teleDic[oldnr]
                else:
                    print("Flera personer har detta namn, ge nummer")

    def save(self, filename):
        f = open(filename, "w")
        for number, names in self.teleDic.items():
            line = number + ";" + ";".join(names) + "\n"
            f.write(line)
            print("Sparar...")

    def load(self, filename):
        self.teleDic = {}
        f = open(filename, "r")
        for line in f:
            line = line.split(";")
            nummer = line[0]
            namn = line[1:]
            self.teleDic[nummer] = namn
            print("Laddar...")


    def remove(self, namn, nr=None):
        nummer = self.find(namn)
        if nummer > 0:
            del self.teleDic[nummer]
            print("Remove done...")
        elif nummer == 0:
            print("Namnet finns inte")
        elif nummer == -1:
            if nr:
                del self.teleDic[nr]
            else:
                print("Flera personer har detta namn, ge nummer")

    def my_quit(self):
        print("Avslutar")
        raise SystemExit



t = TelefonBok()