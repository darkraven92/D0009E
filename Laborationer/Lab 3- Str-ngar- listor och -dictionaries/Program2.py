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
           if addWord not in wordtuple:
               wordlist = list(wordtuple)
               wordlist.append(addWord)
               print(wordlist)
               addDesc = input("Description: ")
               desclist = list(desctuple)
               desclist.append(addDesc)
               print(addDesc)
               print(addWord,":", addDesc,"have been added to the list")
           else:
               print("Word is in list")
       elif ch == "2":
           lookupword = input("Word to lookup: ")
           if lookupword in wordlist:
               print("Description of", lookupword,":",desclist[wordlist.index(lookupword)])
           else:
               print("Word not found")
       elif ch == "3":
           print("Exiting program")
           break
       else:
           print("Not a vaild input")

menu()