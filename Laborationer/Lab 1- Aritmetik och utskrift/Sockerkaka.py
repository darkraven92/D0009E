def recept(antal):
    sockerkaka = [
        "3 dl vetemjöl",
        "2 dl socker",
        f"{2*antal} st ägg",
        "1 dl mjölk",
        "100 g smör",
        "2 tsk bakpulver",
        "1 tsk vaniljsocker"
    ]
    print(f"Recept för {antal} personer:")
    for ingrediens in sockerkaka:
        print(ingrediens)

def tidblanda(antal):
    tid = 10 + antal
    return tid

def tidgradda(antal):
    tid = 30 + 3*antal
    return tid

def sockerkaka(antal):
    recept(antal)
    tid = tidblanda(antal) + tidgradda(antal)
    print(f"Total tid: {tid} minuter")

sockerkaka(4)
print()
sockerkaka(7)
