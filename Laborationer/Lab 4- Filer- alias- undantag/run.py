import re

class Phonebook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, number):
        if name in self.contacts:
            print(f"{name} already exists in the phonebook")
        elif number in [contact["number"] for contact in self.contacts.values()]:
            print(f"{number} already exists in the phonebook with another name")
        else:
            self.contacts[name] = {"number": number, "aliases": set()}
    
    def lookup_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]["number"]
        else:
            print(f"{name} not found in the phonebook")
            return None
    
    def alias_contact(self, name, newname):
        if name in self.contacts:
            self.contacts[name]["aliases"].add(newname)
            self.contacts[newname] = self.contacts[name]
        else:
            print(f"{name} not found in the phonebook")
    
    def change_number(self, name, number):
        if name in self.contacts:
            if number in [contact["number"] for contact in self.contacts.values() if contact != self.contacts[name]]:
                print(f"{number} already exists in the phonebook with another name")
            else:
                self.contacts[name]["number"] = number
        else:
            print(f"{name} not found in the phonebook")
    
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for name, contact in self.contacts.items():
                f.write(f"{name} {contact['number']}\n")
    
    def load_from_file(self, filename):
        with open(filename, "r") as f:
            self.contacts = {}
            for line in f:
                match = re.match(r"(\S+)\s+(\S+)", line)
                if match:
                    self.add_contact(match.group(1), match.group(2))
    
    def run(self):
        while True:
            command = input("telebok> ")
            parts = command.split()
            if not parts:
                continue
            if parts[0] == "add":
                if len(parts) < 3:
                    print("Usage: add name number")
                else:
                    self.add_contact(parts[1], parts[2])
            elif parts[0] == "lookup":
                if len(parts) < 2:
                    print("Usage: lookup name")
                else:
                    name = parts[1]
                    number = self.lookup_contact(name)
                    if number is not None:
                        print(number)
                        for alias in self.contacts[name]["aliases"]:
                            print(alias, number)
            elif parts[0] == "alias":
                if len(parts) < 3:
                    print("Usage: alias name newname")
                else:
                    self.alias_contact(parts[1], parts[2])
            elif parts[0] == "change":
                if len(parts) < 3:
                    print("Usage: change name number")
                else:
                    self.change_number(parts[1], parts[2])
            elif parts[0] == "save":
                if len(parts) < 2:
                    print("Usage: save filename")
                else:
                    self.save_to_file(parts[1])
            elif parts[0] == "load":
                if len(parts) < 2:
                    print("Usage: load filename")
                else:
                    self.load_from_file(parts[1])
            elif parts[0] == "quit":
                break
foo = Phonebook()
foo.run()