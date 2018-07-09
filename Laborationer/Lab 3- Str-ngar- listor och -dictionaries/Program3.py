#Ordlista dictionary

def menu():

    dictionaries = {}
    while True:
       print(""""
       1. Insert
       2. Lookup
       3. Exit
       """)
       ch = input("> ")
       if ch == "1":
           addWord = input("Insert Word: ")
           if addWord not in dictionaries:
               addDesc = input("Description: ")
               dictionaries[addWord] = addDesc
               print(dictionaries)
           else:
               print("Word is in list")
       elif ch == "2":
           lookupword = input("Word to lookup: ")
           for addWord, addDesc in dictionaries.items():
               if addWord == lookupword:
                   print(addWord,":",addDesc)
       elif ch == "3":
           print("Exiting program")
           break
       else:
           print("Invalid input")

menu()
