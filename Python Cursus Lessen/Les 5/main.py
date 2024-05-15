# We importeren hieronder een geheime lijst gevuld met getallen
from hidden import onze_lijst

# > Bereken de som van de lijst genaamd 'onze_lijst'.
# Deze lijst is gevuld met willekeurige getallen
print(type(onze_lijst))
print(type(onze_lijst[0]))

# < CODE HIER >

print(sum(onze_lijst))

# > Schrijf een functie voor het berekenen van het gemiddelde van de elementen in deze lijst en print deze

def averageFromList(list):
    total_num = len(list)
    list_sum = sum(list)
    average = list_sum / total_num
    return average

# > Bekijk of het element op index 5 groter is dan het gemiddelde

# < CODE HIER >

if onze_lijst[5] > averageFromList(onze_lijst):
    print(f"{onze_lijst[5]} is groter dan {averageFromList(onze_lijst)}")
else:
    print(f"{onze_lijst[5]} is kleiner dan {averageFromList(onze_lijst)}")

# > Je kunt hier ook een functie voor schrijven: geef deze functie een positie in de lijst mee, en laat hem controleren of het element op die plek groter is dan het gemiddelde.

# < FUNCTIE HIER >

def isGroterDan(list, index):
    if list[index] > averageFromList(list):
        print(f"{list[index]} is groter dan {averageFromList(list)}")
    else:
        print(f"{list[index]} is kleiner dan {averageFromList(list)}")

isGroterDan(onze_lijst, 5)

# > Wat is het laatste element in de lijst?

# < CODE HIER >

print(onze_lijst[-1])

# > Als je dit nog niet gedaan had: bekijk dit door naar het laatste element in de lijst te kijken zonder de lengte van de lijst te gebruiken.

# < CODE HIER >

# > Wat is het grootste getal in de lijst? Schrijf een functie die  de index op van dit getal teruggeeft

# < FUNCTIE HIER > 

def findLargestNumberPosition(lists):
    largestNumber = max(lists)
    position = lists.index(largestNumber)
    return position

# > Plaats voor en na dit getal een 0, check daarna of dit goed gegaan is
# Dus als 10 het grootste getal is wordt de lijst [..., 0, 10, 0, ...]

# < CODE HIER >

position = findLargestNumberPosition(onze_lijst)
print(position)
onze_lijst.insert(position, 0)
onze_lijst.insert(position+2, 0)
print(onze_lijst)
print(onze_lijst[position])


# > Zoek het grooste nummer deze keer in de lijst door de lijst te sorteren en naar het laatste element te kijken - hiervoor kun je een functie (sort) gebruiken. Vergelijk dit met het grootste getal dat je uit de max functie terugkrijgt

# < CODE HIER >

onze_lijst.sort()
print(onze_lijst[-1])

# Draai de lijst om, zodat nu het kleinste getal achteraan staat. Controleer dit door te kijken of het eerste element nog steeds het grootste element is.

# < CODE HIER >

onze_lijst.sort(reverse=True)
print(onze_lijst[0])

# > Maak nu de lijst leeg

# < CODE HIER >

onze_lijst = list()
print(onze_lijst)
#> Maak een string en vul deze met minimaal 20 letters (hoeft geen bestaand woord o.i.d. te zijn)
# > Vraag met input om een letter en tel hoe vaak die letter in de string staat

#string = "To be or not to be, that is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles."
#letter = input("Welk letter wil je tellen? ")
#print(string.count(letter))

# < CODE HIER >

# Hieronder een lijst met wachtwoorden:
wachtwoorden = [
	'wachtwoord', '1234', '0000', 'mijn_verjaardag', 'naam_van_huisdier',
	'qwerty', 'admin', 'wachtw00rd'
]

# > Vraag een gebruiker om zijn gebruikersnummer (dat is de index (positie) in de lijst)
# > Vraag een gebruiker om zijn wachtwoord
# > Kijk of het wachtwoord klopt
# > Laat de gebruiker het wachtwoord aanpassen
# > Sla deze aanpassing op de goede plek in de lijst op
# > Controleer of het wachtwoord veranderd is

# > Voor extra uitdaging: maak hier functies van/voor


# def inlog(gebruikersnummer, wachtwoord):
#     if wachtwoorden[gebruikersnummer] == wachtwoord:
#         print("Inlog gelukt!")
#         keuze = input("Wil je je wachtwoord aanpassen? (y/n) ")
#         if keuze == "y":
#             nieuwWachtwoord = input("Wat wil je dat je nieuwe wachtwoord is? ")
#             wachtwoordAanpassen(gebruikersnummer, nieuwWachtwoord)
#         else:
#             print("Fijne dag nog!")
#     else:
#         print("Inlog mislukt, probeer het opnieuw!")
        
# def wachtwoordAanpassen(gebruikersnummer, nieuwWachtwoord):
#     wachtwoorden[gebruikersnummer] = nieuwWachtwoord
#     print("Wachtwoord succesvol verandert!")
#     print(wachtwoorden[gebruikersnummer])


# gebruikersnummer = int(input("Wat is je gebruikersnummer? "))
# wachtwoord = input("Wat is je wachtwoord? ")
# inlog(gebruikersnummer, wachtwoord)