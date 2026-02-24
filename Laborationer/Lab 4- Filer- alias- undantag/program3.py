#!/usr/bin/env python3
import sys

class PhoneBook:
    def __init__(self):
        self.book = {}

    def add(self, name, number):
        if name in self.book:
            return f"Error: '{name}' already exists"
        if any(obj['num'] == number for obj in self.book.values()):
            return f"Error: number '{number}' already in use"
        obj = {'num': number}
        self.book[name] = obj

    def lookup(self, name):
        if name not in self.book:
            return f"Error: '{name}' not found"
        print(self.book[name]['num'])

    def alias(self, name, newname):
        if name not in self.book:
            return f"Error: '{name}' not found"
        if newname in self.book:
            return f"Error: '{newname}' already exists"
        self.book[newname] = self.book[name]

    def change(self, name, number):
        if name not in self.book:
            return f"Error: '{name}' not found"
        if any(obj is not self.book[name] and obj['num'] == number for obj in self.book.values()):
            return f"Error: number '{number}' already in use"
        self.book[name]['num'] = number

    def save(self, filename):
        try:
            groups = {}
            for name, obj in self.book.items():
                groups.setdefault(id(obj), (obj['num'], []))[1].append(name)
            with open(filename, 'w') as f:
                for num, names in groups.values():
                    f.write(num + ';' + ';'.join(names) + ';\n')
        except IOError as e:
            return f"Error: {e}"

    def load(self, filename):
        try:
            new_book = {}
            with open(filename) as f:
                for line in f:
                    parts = line.strip().rstrip(';').split(';')
                    if len(parts) < 2: continue
                    num, *names = parts
                    obj = {'num': num}
                    for name in names:
                        new_book[name] = obj
            self.book = new_book
        except IOError as e:
            return f"Error: {e}"

def main():
    pb = PhoneBook()
    prompt = "telebok> "
    cmds = {
        'add':    lambda a: pb.add(*a) if len(a)==2 else "Usage: add name number",
        'lookup': lambda a: pb.lookup(*a) if len(a)==1 else "Usage: lookup name",
        'alias':  lambda a: pb.alias(*a) if len(a)==2 else "Usage: alias name newname",
        'change': lambda a: pb.change(*a) if len(a)==2 else "Usage: change name number",
        'save':   lambda a: pb.save(*a) if len(a)==1 else "Usage: save filename",
        'load':   lambda a: pb.load(*a) if len(a)==1 else "Usage: load filename",
        'quit':   lambda a: sys.exit(0),
    }
    while True:
        try:
            line = input(prompt).split()
        except (EOFError, KeyboardInterrupt):
            break
        if not line: continue
        cmd, *args = line
        if cmd not in cmds:
            print(f"Error: unknown command '{cmd}'")
        else:
            result = cmds[cmd](args)
            if result: print(result)

if __name__ == '__main__':
    main()
