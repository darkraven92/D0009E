Lab 3
Uppgift 0 (behöver ej redovisas)
Skapa ett program som implementerar ett enkelt menysystem för uppgifterna från lab 2. Programmet ska presentera en meny med fyra alternativ som utför följande uppgifter:
fråga efter en parameter till bounce och kör sedan bounce med denna parameter
fråga efter en parameter till tvärsumman och kör sedan tvärsumman med denna parameter
fråga efter ett startvärde till newton-raphson och lös sedan f(x)=x^2-1 genom att anropa newton-raphson från lab 2.
avsluta programmet.
Efter att en av uppgifterna utförts så ska menyn visas igen (utom för alternativert "avsluta programmet"). När man implementerar en meny är det lämpligt att använda en iterativ metod för att visa menyn. Detta eftersom menyn kan visas godtyckligt många gånger och en rekursiv metod då upptar succesivt mer minne.
Ordlista
I denna laboration ska vi implementera en enkel ordlista m.h.a. python. Ordlistan ska vara interaktiv och användaren ska kunna lägga till och slå upp ord i ordlistan. Själva ordlistan ska implementeras på tre olika sätt, med tre olika sätt att spara ordlistan. Följande tre olika sätt att lagra en ordlista implementeras:
Två stycken listor av strängar. Den första listan innehåller ordet vi vill slå upp, och den andra listan innehåller beskrivningen för det ordet, på motsvarande position.
En lista av tupler. En enda lista som består av par, där första delen av varje par är ordet vi vill slå upp, och den andra är beskrivningen. Observera här altlså att datastrukturen ska vara  en lista, varje element i denna lista ska i sin tur vara ett par (en tupel med två element).
Ett dictionary. Ett dictionary som innehåller ordet vi vill slå upp som "nyckel" och tillhörande beskrivning som "värde".
För varje lösning ska två operationer finnas: en för att sätta in och en för att slå upp ord i listan. Återanvänd gärna kod mellan de tre lösningarna (t.ex. kan du ha samma funktion som skriver ut själva menyn). Separera de tre lösningarna genom att välja olika namn på funktionerna. Varje lösning ska ha en egen funktion som startar just den lösningen.

Ordlistan ska presentera användaren med en meny där det finns följande alternativ: 1: Insert, 2: Lookup. Användaren ska kunna välja alternativ genom mata in siffran för motsvarande operation. Programmet ska sedan fråga användaren efter vilket ord operationen ska verka på och sedan, i fallet med insert fråga efter ordets beskrivning. Det ska inte vara tillåtet att sätta in samma ord två gånger i ordlistan. Om användaren försöker göra det ska ett felmeddelande skrivas ut. I fallet med lookup ska beskrivningen för ordet, som finns lagrad, skrivas ut på skärmen. Om ordet som slås upp inte existerar i ordlistan så ska ett felmeddelande skrivas ut.

Exempel på körning:
>>> main_dic()
Menu for dictionary

 1: Insert
 2: Lookup
 3: Exit program

Choose alternative: 1
Word to insert: dator
Description of word: en manick som inte fungerar
Menu for dictionary

 1: Insert
 2: Lookup
 3: Exit program

Choose alternative: 2
Word to lookup: dator
Description for dator : en manick som inte fungerar
Menu for dictionary

 1: Insert
 2: Lookup
 3: Exit program

Choose alternative: 3
>>> 
Frivillig extrauppgift: Lägg till funktionen "delete" i menyerna och implementera den. Funktionen tar bort ord (och beskrivning) från ordlistan.
