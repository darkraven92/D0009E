def main_dic():
    word = []
    description = []

    while True:
        print
        "\n Meny för ordlista \n 1: Sätta in \n 2: Slå upp \n 3: Stäng program \n"
        val = input('Välj Alternativ:')
        if val == '1':
            x = input('Ordet som ska sättas in:')
            if x in word:
                print
                "Ordet finns redan i listan."
            else:
                y = input('Beskrinving av ord:')
                word.append(x)
                description.append(y)

        elif val == '2':  # Letar upp ordet
            z = input('Ord som söks:')
            if z in word:
                print
                "Beskrivningen av: ", z, "är", description[:]
            else:
                print
                "Kunde inte hitta ordet:", z

        elif val == '3':
            break

main_dic()
