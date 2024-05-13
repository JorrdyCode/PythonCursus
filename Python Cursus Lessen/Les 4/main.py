
# In deze opdracht gaan we een aantal dingen oefenen met functies
# Ook zal je code die je eerder hebt geschreven voor een opdracht om gaan zetten
# naar functies, zodat deze eventueel makkelijker gebruikt kunnen worden

# In opdracht 2 hebben jullie een fizzbuzz programma geschreven
# We konden daarin de % operator gebruiken om te controleren of getal X
# volledig deelbaar was door getal Y.
# Schrijf een functie die deze controle voor jou uitvoert. Wat heb je hier voor nodig?
# > Wat ga je de functie meegeven?
# > Wat gaat de functie teruggeven?
# > Wat gebeurt er binnen de functie om van de parameters de return waarde te maken?
# Als uitkomst zouden we dus iets willen kunnen doen als:

# print(fullyDivisble(15,3)) # Dus, is 15 volledig deelbaar door 3?
# >>> True
# print(fullyDivisible(16,3))
# >>> False

# We hebben het ook kort gehad over functie compositie, dus het combineren van
# functies om ingewikkelder gedrag voor elkaar te krijgen
# > Maak een functie die het hele fizzbuzz programma voor je kan uitvoeren. Maak hiervoor
# gebruik van de functie die je bij de vorige opdracht hebt geschreven
# Voorbeeld output:

# print(fizzbuzz(12))
# >>> Fizz
# print(fizzbuzz(15))
# >>> Fizzbuzz
# print(fizzbuzz(20))
# >>> Buzz
# print(fizzbuzz(4))
# >>> 4

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if number % 3 != 0 and number % 5 != 0:
        result = number
    return result

print(fizzbuzz(12))
print(fizzbuzz(15))
print(fizzbuzz(20))
print(fizzbuzz(4))

# In opdracht 3 hebben we bijvoorbeeld laten printen hoe vaak elke klinker in een 
# gegeven stuk tekst voorkwam. Hiervoor maakten we gebruik van string.count(klinker) functie
# Deze moesten we alleen iedere keer handmatig 5 keer uitschrijven - en als we dit willen
# printen voor een ander stuk tekst moet je ze nóg een keer 5 keer uitschrijven. Daar kunnen
# we een functie voor maken!

# Schrijf een functie die een stuk tekst meekrijgt, en dan voor die tekst afdrukt hoe vaak
# elke klinker voorkomt.
# Bedenk weer goed wat deze functie mee moet krijgen en wat deze gaat teruggeven. 
# Voorbeeld output:

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def telKlinkers(tekst):
    tekst.lower()
    a_num = tekst.count("a")
    u_num = tekst.count("u")
    o_num = tekst.count("o")
    e_num = tekst.count("e")
    i_num = tekst.count("i")
    print(f"a komt {a_num} keer voor.")
    print(f"u komt {u_num} keer voor.")
    print(f"o komt {o_num} keer voor.")
    print(f"e komt {e_num} keer voor.")
    print(f"i komt {i_num} keer voor.")

# print(telKlinkers(tekst))
# >>> A komt 5 keer voor
# >>> U komt 2 keer voor
# >>> O komt 12 keer voor
# >>> E komt 6 keer voor
# >>> I komt 0 keer voor

telKlinkers(text)

# Maak hiervoor ook zelf een variabele met een wat langer stukje tekst aan