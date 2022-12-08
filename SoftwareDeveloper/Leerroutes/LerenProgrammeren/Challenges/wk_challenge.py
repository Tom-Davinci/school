GEWONNEN = 3

def intinput():
    while True:
        try:
            x = int( input("Voer een nummer in: "))
            return x
        except:
            print("Voer een geldig nummer in")

groepA = []
while True:
    land = input("Voer hier een land in\n").upper()
    if land not in groepA:
        groepA.append(land)
        if len(groepA) >= 3:
            break
    else:
        print("Nieuw land invoeren!")

teams = []
for x in range( len(groepA)):
    teams.append({
        "name" : groepA[x],
        "punten" : 0,
        "doelsaldo" : 0
        })

rondes = 1
t1 = -1
t2 = 0


while rondes < 3:
    t1 += 1
    t2 += 1

    print(f"Wedstrijd {rondes} score {groepA[t1]} - {groepA[t2]}")
    print(f"Score {groepA[t1]}")
    score1 = intinput()
    print(f"Score {groepA[t2]}")
    score2 = intinput()

    if score1 > score2:
        doelsaldo = score1 - score2
        teams[t1]["punten"] += GEWONNEN
        teams[t1]["doelsaldo"] += doelsaldo
        teams[t2]["doelsaldo"] -= doelsaldo
    else:
        doelsaldo = score2 - score1
        teams[t2]["punten"] += GEWONNEN
        teams[t2]["doelsaldo"] += doelsaldo
        teams[t1]["doelsaldo"] -= doelsaldo

    print(f"Wedstrijd {groepA[t1]} - {groepA[t2]} eindigde in {score1} - {score2}")
    rondes += 1


print("overzicht groep A")
for i in range( len(groepA)):
    naam = teams[i]["name"]
    punten = teams[i]["punten"]
    doelsaldo = teams[i]["doelsaldo"]
    print(f"{naam}: punten {punten}; doelsaldo: {doelsaldo}")