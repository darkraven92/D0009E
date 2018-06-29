Lab 1
Aritmetik och utskrift

Det här är den första "riktiga" labben, och den är tänkt att tjäna som en introduktion till Python och utvecklingsmiljön IDLE samt funktionsbegreppet.
Det vi i första hand ska öva på är användande av Pythons operatorer för hel- och flyttalsaritmetik samt utskrift av text på skärmen och funktionsanrop.

Tips: glöm inte att Python-filerna skall ha ändelsen .py 
Uppgifterna
Uppgift 1
Definiera en funktion recept(antal), som skriver ut en lista på ingredienser till en sockerkaka som är lagom 
för det givna antalet personer. Följande recept är lämpligt för 4 personer. Observera att din funktion måste fungera för godtyckiligt antal personer. I utskriften ska antalet ägg vara heltal. För väldigt få personer kan det hända att man får 0 ägg. Detta beteende är acceptabelt.
Definiera två olika funktioner för tidsåtgång vid tillagning av sockerkaka:
En funktion tidblanda(antal) som beräknar och returnerar tiden för att blanda smeten till en sockerkaka för antal personer. Tidsåtgången ska beräknas som 10 minuter fast tid (oavsett antal personer) samt dessutom ytterligare en minut för varje person kakan är avsedd för.
En funktion tidgradda(antal) som beräknar och returnerar tiden för att grädda kakan, Tidsåtgången ska beräknas som 30 minuter fast tid (oavsett antal personer) samt dessutom ytterligare 3 minuter för varje person kakan är avsedd för.

Definiera en funktion sockerkaka(antal) som skriver ut recept för antal personer på skärmen samt tidsåtgång för antal personer. I tidsåtgången ska både tid för gräddning och blandning inkluderas i samma värde (summeras). Funktionerna från (1) och (2) ska användas.
Skriv, i samma fil, ett script som skriver ut sockerkaksrecept till 4 och 7 personer på skärmen. Programmet ska alltså skriva ut två recept efter varandra. Här är det noga med att du skriver just ett script, inte en till funktion. Scriptet ska däremot använda din funktion från uppgift 3.
Uppgift 2
En variant att betala av ett lån är att använda s k rak amortering. Detta innebär att själva skulden betalas av i ett antal 
lika stora poster, och att räntekostnaden, som ju beräknas på den kvarvarande skulden, således blir succesivt lägre vid 
varje betalning. Den totala kostnaden k för ett lån (dvs all amortering plus total räntekostnad) kan med rak amortering
beräknas med följande formel,
        k = P + (a+1)Pr/2
där P är det lånade beloppet, r är den årliga räntesatsen och a är antal år för återbetalning.
Skriv en funktion kostnad(P, r, a) som beräknar och skriver ut den totala kostnaden för ett lån enligt formeln 
ovan. Denna funktion ska sparas i en separat fil (inte samma som uppgift 1 och 2). En exempelkörning av funktionen ska kunna se ut så här:
>>> kostnad(50000, 0.03, 10)
Den totala kostnaden efter 10 år är 58250 kr. 
