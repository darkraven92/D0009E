from pathlib import Path

class Kontakt:
    def __init__(self, nr: str, namn: set[str]):
        self.nr = nr
        self.namn = namn

class Telefonbok:
    def __init__(self):
        self.namn_db: dict[str, list[Kontakt]] = {}
        self.nr_db: dict[str, Kontakt] = {}

    def _hitta(self, namn: str, nr: str = None) -> Kontakt:
        träffar = self.namn_db.get(namn)
        if not träffar: raise ValueError("Fel: Namnet saknas.")
        if len(träffar) > 1:
            if not nr: raise ValueError("Fel: Flera träffar. Ange nummer.")
            träffar = [k for k in träffar if k.nr == nr]
            if not träffar: raise ValueError("Fel: Inget matchande nummer.")
        return träffar[0]

    def add(self, namn: str, nr: str):
        if nr in self.nr_db: raise ValueError("Fel: Numret finns redan.")
        k = Kontakt(nr, {namn})
        self.nr_db[nr] = k
        self.namn_db.setdefault(namn, []).append(k)

    def lookup(self, namn: str):
        if namn not in self.namn_db: raise ValueError("Fel: Namnet saknas.")
        for k in self.namn_db[namn]: print(k.nr)

    def alias(self, namn: str, nytt_namn: str, nr: str = None):
        k = self._hitta(namn, nr)
        if nytt_namn not in k.namn:
            k.namn.add(nytt_namn)
            self.namn_db.setdefault(nytt_namn, []).append(k)

    def change(self, namn: str, nytt_nr: str, glt_nr: str = None):
        k = self._hitta(namn, glt_nr)
        if nytt_nr in self.nr_db: raise ValueError("Fel: Nya numret används redan.")
        del self.nr_db[k.nr]  
        k.nr = nytt_nr
        self.nr_db[nytt_nr] = k 

    def remove(self, namn: str, nr: str = None):
        k = self._hitta(namn, nr)
        del self.nr_db[k.nr]
        for n in k.namn:
            self.namn_db[n].remove(k)
            if not self.namn_db[n]: del self.namn_db[n]

    def save(self, fil: str):
        text = "".join(f"{k.nr};{';'.join(k.namn)};\n" for k in self.nr_db.values())
        Path(fil).write_text(text, "utf-8")

    def load(self, fil: str):
        p = Path(fil)
        if not p.is_file(): raise ValueError("Fel: Filen hittades inte.")
        self.__init__() 
        for r in p.read_text("utf-8").splitlines():
            if delar := [x for x in r.split(';') if x]:
                nr, namn_lista = delar[0], set(delar[1:])
                k = Kontakt(nr, namn_lista)
                self.nr_db[nr] = k
                for n in namn_lista: self.namn_db.setdefault(n, []).append(k)

if __name__ == "__main__":
    tb = Telefonbok()
    kommandon = {
        "add": tb.add, "lookup": tb.lookup, "alias": tb.alias, 
        "change": tb.change, "remove": tb.remove, "save": tb.save, "load": tb.load
    }
    
    while True:
        try:
            inmatning = input("telebok> ").split()
            if not inmatning: continue
            
            kommando, *argument = inmatning
            
            if kommando == "quit": break
            if kommando in kommandon:
                kommandon[kommando](*argument)
            else:
                print("Fel: Okänt kommando.")
                
        except TypeError:
            print("Fel: Fel antal argument för kommandot.")
        except ValueError as e:
            print(e)
        except (EOFError, KeyboardInterrupt):
            print()
            break
