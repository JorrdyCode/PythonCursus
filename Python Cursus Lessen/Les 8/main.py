# > Schrijf een functie die returnt of een key in een dictionary zit of niet (True of False)

taart_dict = {'appeltaart' : 'goed', 'slagroomtaart' : 'slecht' }

def is_key_in_dict(naam, my_dict):
    return naam in my_dict
    # Vul hier code in

print(is_key_in_dict('appeltaart', taart_dict))
print(is_key_in_dict('frambozenvlaai', taart_dict))

# # > Schrijf een functie die returnt of een bepaalde value in een dictionary zit of niet

def is_value_in_dict(naam, my_dict):
    return naam in my_dict.values()

print(is_value_in_dict('goed', taart_dict))
print(is_value_in_dict(42, taart_dict))

# # > Schrijf een functie die een naam meekrijgt en een geformatteerde string terug geeft van de naam van de persoon en het bijbehorende cijfer. Als de persoon niet in de lijst staat, geef dan een string terug die dit duidelijk maakt.

cijfers = {'Robert': 10, 'Nick': 10, 'Jan': 'Onvoldoende', 'Vera': 10}

def geef_naam_en_cijfer(naam, dicts):
    if is_key_in_dict(naam, dicts):
        return f"{naam} heeft een {cijfers[naam]}."
    else:
        return f"{naam} is niet bekend bij ons."

print(geef_naam_en_cijfer('Vera',cijfers))
print(geef_naam_en_cijfer('Florian',cijfers))

# # > Schrijf een functie die de gemiddelde leeftijd van alle auto's in de dictionary berekent.

car_database = {'DeLorean DMC-12': 1981, 'Ford Mustang': 1964, 'Ford F150': 1948, 'Ford Ka': 1996, 'Bugatti type 55': 1931, 'Tesla Roadster': 2008, 'Tesla Model 3': 2016, 'Ford focus': 1998}

def carAgeAvg(database):
    sum = 0
    for car in database:
        sum += 2024 - database[car]
    return sum / len(database)

print(carAgeAvg(car_database))


# # In voorgaande opdrachten hebben we een aantal keer alle klinkers in een stuk tekst geteld. Dit gaan we nu nog een keer doen, maar dan met een dictionary.
# # > Herschrijf je functie van vorige les, waarbij je een stuk tekst en een aantal letters door kon geven om deze te tellen, zodat deze nu een dictionary teruggeeft die de letters als key heeft en als value hoe vaak deze letter voor is gekomen. 

def getelde_letters(text, letters):
    letter_freq = dict()
    for letter in text:
        if letter in letters:
            if is_key_in_dict(letter, letter_freq):
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
    return letter_freq