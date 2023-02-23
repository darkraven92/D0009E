def list_dict():
    # Create empty lists for words and descriptions
    words = []
    descriptions = []

    # Menu loop
    while True:
        print("Menu for dictionary")
        print("1: Insert 2: Lookup 3: Exit program")

        # Get user choice
        choice = input("Choose alternative: ")

        # Insert operation
        if choice == "1":
            word = input("Word to insert: ")

            # Check if word is already in list
            if word in words:
                print("Error: Word already exists in list")
                continue

            description = input("Description of word: ")

            # Add word and description to lists
            words.append(word)
            descriptions.append(description)

        # Lookup operation
        elif choice == "2":
            word = input("Word to lookup: ")

            # Find index of word in list
            try:
                index = words.index(word)
            except ValueError:
                print("Error: Word not found in list")
                continue

            # Print description
            print(f"Description for {word}: {descriptions[index]}")

        # Exit program
        elif choice == "3":
            break

        # Invalid choice
        else:
            print("Error: Invalid choice")

    print("Exiting program")


#list_dict()
def tuple_list_dict():
    # Create empty list for word-description pairs
    word_desc_pairs = []

    # Menu loop
    while True:
        print("Menu for dictionary")
        print("1: Insert 2: Lookup 3: Exit program")

        # Get user choice
        choice = input("Choose alternative: ")

        # Insert operation
        if choice == "1":
            word = input("Word to insert: ")

            # Check if word is already in list
            for pair in word_desc_pairs:
                if pair[0] == word:
                    print("Error: Word already exists in list")
                    break
            else:
                description = input("Description of word: ")

                # Add word-description pair to list
                word_desc_pairs.append((word, description))

        # Lookup operation
        elif choice == "2":
            word = input("Word to lookup: ")

            # Find description for word in list
            for pair in word_desc_pairs:
                if pair[0] == word:
                    print(f"Description for {word}: {pair[1]}")
                    break
            else:
                print("Error: Word not found in list")

        # Exit program
        elif choice == "3":
            break

        # Invalid choice
        else:
            print("Error: Invalid choice")

    print("Exiting program")

    tuple_list_dict()