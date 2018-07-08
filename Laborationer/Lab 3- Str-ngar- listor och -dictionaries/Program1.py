#Ordlista listor

def menu():
   wordliststr = []
   descliststr = []

   while True:

       print(""""
       1. Insert
       2. Lookup
       3. Exit
       """)


       ch = input("> ")
       if ch == "1":
           addWord = input("Insert word: ")
           if addWord not in wordliststr:
               wordliststr.append(addWord)
               print(wordliststr)
               addDesc = input("Add description: ")
               descliststr.append(addDesc)
           else:
               print("Word is in list")
       elif ch == "2":
           lookupword = input("Word to lookup: ")
           if lookupword in wordliststr:
               print("Description for",lookupword,":",descliststr[wordliststr.index(lookupword)])
           else:
               print("Word not found")
       elif ch == "3":
           print("Exiting program")
           break
       else:
           print("Enter a vaild input")

menu()








