from hidden import shuffle, is_sorted, secret_number

#   __ _ _   _  ___  ___ ___
#  / _` | | | |/ _ \/ __/ __|
# | (_| | |_| |  __/\__ \__ \
#  \__, |\__,_|\___||___/___/
#  |___/

# hidden.py geeft jullie een geheim nummer genaamd `secret_number`, dit is iedere keer dat je het runt anders. Schrijf een programma met een while loop welke de gebruiker 3 pogingen geeft om het getal te raden. Als de gebruiker het getal niet goed raad vertel dan of het groter of kleiner is dan het geheime getal
# hint gebruik de if,elif,else constructie die we eerder hebben geleerd

guess = 1
while True:
    answer = int(input("Welk getal? "))
    if answer == secret_number:
        print("Goed geraden!")
        break
    elif guess == 3:
        print("Fout geraden, het antwoord was ", secret_number)
        break
    guess += 1




#      _  _  __
#  ___(_)(_)/ _| ___ _ __ ___
# / __| || | |_ / _ \ '__/ __|
#| (__| || |  _|  __/ |  \__ \
# \___|_|/ |_|  \___|_|  |___/
#      |__/

# > Vraag een gebruiker d.m.v. een while loop om cijfers van zijn studenten (komma getallen van 1 t/m 10)
# > Check eventueel of het ingevoerde getal wel tussen de 1 en 10 ligt!
# > Sla deze op in een lijst
# > Als de gebruiker 0 invoert is hij klaar met de lijst vullen.

# Nu we een lijst van cijfers hebben kunnen we daar dingen mee berekenen
# > Bereken met behulp van een for loop het aantal elementen in de lijst:
# > maak een variabele voor de lengte

# > Bereken door een for loop te gebruiken het gemiddelde van de cijfers:
# > maak een variabele
# > gebruik een for loop om daar ieder cijfer bij op te tellen
# > als dat klaar is deel het door het aantal getallen in de lijst

# > Bereken door één for loop te gebruiken de volgende drie dingen: hoeveel voldoendes er zijn, het minimum en het maximum in de lijst:
# > Gebruik drie variabelen een voor de hoeveelheid voldoendes, een voor het minimum en een voor het maximum
# > Gebruik in je for loop drie if statements (sowieso één voor het minimum en één voor het maximum)

# > print nu de statistieken over deze cijfers die je net hebt berekend

grades = list()

while True:
    studentnumber = int(input("Geef het cijfer van je studenten, typ 0 om te eindigen."))
    if studentnumber == 0:
        break
    if studentnumber > 0:
        grades.append(studentnumber)

length = 0
for number in grades:
    length += 1  

sum = 0
for number in grades:
    sum += number
average = sum / length

voldoendes = 0
minimum = 10
maximum = 0

for number in grades:
    
    if number > 6:
        voldoendes += 1
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print(grades)
print(length)  
print(average)
print(voldoendes)
print(maximum)
print(minimum)

        


#      _            __  __ _
#  ___| |__  _   _ / _|/ _| | ___
# / __| '_ \| | | | |_| |_| |/ _ \
# \__ \ | | | |_| |  _|  _| |  __/
# |___/_| |_|\__,_|_| |_| |_|\___|
#

# shuffle sort
# shuffle sort is een van de minst efficiente sort algoritmen dat er is
# het gaat als volgt te werk:
# > Neem een lijst met getallen (bijvoorbeeld de lijst die je in de vorige opdracht hebt gemaakt)
# > Shuffle deze random door elkaar (als het schudden van een pakje kaarten)
# > Kijk of de lijst gesorteerd is
# > Is de lijst gesorteerd ben je klaar, is deze niet gesorteerd shuffle dan nog een keer
#
# Wij hebben de lastigere onderdelen al geschreven voor jullie:
# gebruik de volgende functie om te kijken of een lijst gesorteerd is
# `is_sorted(lijst)` > Deze returnt True als de lijst gesorteerd is en False als dat niet het geval is.
# gebruik deze functie om een lijst te schudden
# `shuffle(lijst)` > deze verandert de bestaande lijst
#
# Om te kijken hoe het sorteren gaat kun je tussendoor je lijst printen

while not is_sorted(grades):
    print(grades)
    shuffle(grades)

print(grades)