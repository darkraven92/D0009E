#Ordlista tupler

def menu():
    wordtuple = ()
    desctuple = ()
    while True:
       print(""""
       1. Insert
       2. Lookup
       3. Exit
       """)
       ch = input("> ")
       if ch == "1":
           addWord = input("Insert word: ")
           wl = list(wordtuple)
           dl = list(desctuple)
           if addWord not in wl:
               wl.append(addWord)
               addDesc = input("Description: ")
               dl.append(addDesc)
               print(addWord,":", addDesc,"have been added to the list")
           else:
               print("Word is in list")
       elif ch == "2":
           lookupword = input("Word to lookup: ")
           wl = list(wordtuple)
           dt = list(desctuple)
           if lookupword in wordtuple:
               print("Description of", lookupword,":",dt[wl.index(lookupword)])
           else:
               print("Word not found")
       elif ch == "3":
           print("Exiting program")
           break
       else:
           print("Not a vaild input")

menu()