Lab 4
Uppgift 0 (behöver ej redovisas)
Vi ska implementera ett system som simulerar två anslagstavlor och två personer som kan stå framför endera tavlan (de kan stå framför samma tavla). Personerna kan sätta upp ett nytt meddelande på tavlan de står framför.
Deklarera en klass, Board, som innehåller en konstruktor som initierar variabeln message till värdet av parametern msg, (initieraren tar då två paramtetrar, dels self och så msg). Denna klass representerar klassen av anslagstavlor, och instanser (objekt) representerar en anslagstavla.
Deklarera en funktion, main(), som skapar två instanser av klassen Board och presenterar en meny liknande följande:
=== Bulletin board system ===
Kim reads message: Board1: 
Chris reads message: Board2: 
1: Direct Kim to other board
2: Direct Chris to other board
3: Tell Kim to post a message
4: Tell Chris to post a message
0: exit
Enter choice:
Använd två variabler, kim och chris, som är alias för en instans av Board.
De första två raderna visar vad Kim och Chris ser för tillfället. När kim eller chris lägger till ett meddelande till anslagstavlan så konkatenerars lämpligen den tillagda texten till den gamla.
En telefonbok
Glöm inte att beakta kodstilen i denna lab. Denna laboration syftar till att öva användning av dictionaries och objekt (även om detta inte är ett krav), i synnerhet vad gäller hantering av alias. Dessutom kommer programmet som ska skrivas att vara interaktivt. Viss rudimentär felhantering kommer också att behövas, men om detta ska implementeras med hjälp av Python's exceptions är en designfråga där beslutet är ert eget.

Laborationsuppgiften är att skriva ett interaktivt program som hanterar en dynamisk telefonbok via en uppsättning enkla kommandon (dynamisk betyder att det går att ändra i telefonboken). Kommandona ska alla vara en rad långa och kunna updelas i ord med whitespace emellan (ett eller flera whitespace ska accepteras av programmet).  Telefonboken kan antingen användas till gamla hederliga fasta telefoner (en antik företeelse som existerade förra seklet) eller till att hantera mer moderna mobiltelefoner som har tvillingkort (där då fler telefoner får samma nummer). Prompten kan vara helt valfri (prompt=det som skrivs ut innan programmet väntar på inmatning från användaren). Följande kommandon ska hanteras (fler får läggas till efter behag):
add name number – lägger till name med nummret number till telefonboken. Här är det tillåtet att begränsa sig till att namn måste vara unika (två olika personer med olika nummer kan inte heta likadant). Alla telefonnummer måste vara unika; det är alltså inte tillåtet att lägga till flera namn med samma telefonnummer som inte är alias (alias har alltid, per konstruktion, samma telefonnummer).
lookup name – skriver ut numret som finns lagrat för name.
alias name newname – låter name bli sökbart även under namnet newname. Observera att name och newname blir helt likställda - newname fungerar i alla avseenden som name.
change name number – ändrar numret som associeras med det befintliga namnet name till number.
save filename – sparar innehållet i telefonboken till filen filename.
load filename – läser in innehållet från filen filename till telefonboken. Telefonboken i minnet kastas bort (efter inläsningen har vi endast telefonboken från filen i minnet).
quit – avslutar den interaktiva körningen
För kommandot add gäller att en felutskrift ska genereras om name redan finns definierat i telefonboken; för de övriga gäller att felutskrift ska ske om name inte är definierat. Med felutskrift menas att programet ska berätta vad som är fel på ett begripligt sätt och sedan skriva ut prompten igen. Namn som definierats som alias (med alias-kommandot) ska kunna användas i lookup-, change- och andra alias-kommandon på samma sätt som alla namn, så att följande beteende erhålls:

telebok> add peter.forsberg 12345
telebok> lookup peter.forsberg
12345
telebok> alias peter.forsberg foppa
telebok> lookup foppa
12345
telebok> alias foppa MR21
telebok> change MR21 67890
telebok> lookup peter.forsberg
67890

Notera att programmet ska presentera en prompt ("telebok>" i det här fallet") och att användaren sedan ska kunna skriva ovanstående kommandon på beskrivet sätt. Det är inte tillåtet att ha en meny i denna uppgift.
Ett telefonnummer lagras lämpligtvis som en sträng. Ingen speciell kontroll av formatet på telefonnumret behöver göras (om användaren är dum nog att skriva in nåt annat än ett telefonnummer så tillåts det också).
Ytterligare ett textexempel med en sparfil finns.
Load och save (filformat) - förenklad version:
Det är tillåtet att ignorera alias när man sparar till och laddar från fil. Filformatet är som följer: På varje rad i filen ska ett telefonnummer sparas först på raden, åtföljt av ett semikolon och sedan åtföljt av namnet som motsvarar telefonnumret fölt av semikolon. Om det alltså råkar finnas alias för namnet så sparar man detta på en egen rad, fast med samma telefonnummer. Vi får då en rad per namn i filen (ingen skillnad på "namn" och "alias"). Man behöver då inte ta hänsyn till alias när man sparar, vilket förenklar en hel del. När man laddar in en sådan fil (använder load) får man naturligtvis inte tillbaka aliasen, utan varje namn upptäder då i telefonboken som ett eget namn med eget telefonnummer (som råkar vara samma telefonnummer som någon anna, som tidigare var alias). Exempel (samma telefonbok som ovan):

123;Kalle;
123;Maria;
321;Anna;
321;Olle;

Internt i programmet är det lämpligt att använda ett dictionary som central datastruktur. Det finns dock all anledning att inte låta detta dictionary lagra telefonnummer direkt som värde, utan att blanda in muterbara datastrukturer (t ex objekt) som mellansteg (detta är den enklaste lösningen). Det är också starkt rekommenderat att inte göra någon skillnad överhuvudtaget på namn och alias; ett alias är bara ett till namn för samma nummer. Det interaktiva beteendet åstadkoms enklast genom att en loop (lämpligen while) börjar varje varv med att anropa raw_input(), varefter resultatet analyseras och motsvarande kommando utförs (tänk på att detta inte går att göra rekursivt, eftersom vi potentiellt kör gopdtyckligt många varv, vilket skulle fylla upp minnet). Försök separera ut kommandon så att dessa implementeras i separata funktioner.
Extrauppgifter (lösning av samtliga extrauppgifter ger 5 % av poängen på tentan)
I denna extrauppgift är det tillåtet att ha flera personer med samma namn, däremot får dessa inte dessutom ha samma telefonnummer (de går då inte att särskilja visar det sig).
Ändra implementationen av load och save så att den fullständiga versionen implementeras (inte den förenklade) enligt följande:
Load och save (filformat) - fullständig version:
För kommandona save och load ska följande filformat användas (det ska alltså se ut så här i filen som skapas): Varje rad i filen motsvarar ett telefonnummer. Varje rad börjar med telefonnumret åtföljt av semikolon. Därefter följer en lista av de namn (inkl. alias) som har numret för raden, namnen ska vara årskilda av semikolon.   Exempel:

123;Kalle;Maria;
321;Anna;Olle;
Ändra implementationen så att det blir tillåtet att ha samma namn flera gånger (personer kan heta likadant). En sökning (lookup) på ett sådant namn ska ge telefonnumren till samtliga personer som har det sökta namnet.
Ändra kommandona alias och change så att dessa tar ett extra argument, telefonnummer. Detta används för att särskilja namn som är samma. Argumentet ska vara det sista argumentet på raden och behöver endast ges om det finns flera likadana namn som det sökta namnet. Om argumentet inte ges och det finns flera namn som det sökta så ska ett felmeddelande skrivas ut.
Implementera kommandot remove name number, som tar bort namnet name med alla dess alias samt motsvarande telefonnummer, under förutsättning att name är tidigare definierat. Parametern number används för att särskilja olika personer med samma namn. Den behöver endast anges då det finns flera personer med samma namn.
Tips: Det kan vara enklast att helt byta intern representation för att lösa dessa uppgifter (inte använda dictionary).
