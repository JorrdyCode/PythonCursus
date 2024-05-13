# bot.py

import discord
import os
import json
from helpers import reply_to_self, upside_down, USERNAME, TOKEN
from random import randint, choice

# Vul deze 2 waarden zelf in in helpers.py. Je username vind je in Discord dit is je unieke user ID (lang getal in de vorm 123457890123456789), je token in het Discord Developer portal:
# https://discord.com/developers/applications
_TOKEN = TOKEN
_USERNAME = USERNAME

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

CostToLevel = {
  1: 100,
  2: 150,
  3: 200,
  4: 250,
  5: 300
}

def resetStats(equippedItem):

  with open("data.json") as file:
    source = json.load(file)
    Players = source["Players"]["Registered"]
    Equipment = source["Equipment"]["Weapon"]

  Players["Jordy"]["Attack"] -= Equipment[equippedItem]["Attack Power"]
  Players["Jordy"]["Strength"] -= Equipment[equippedItem]["Strength Bonus"]
  Players["Jordy"]["Agility"] -= Equipment[equippedItem]["Agility Bonus"]
  Players["Jordy"]["Intelligence"] -= Equipment[equippedItem]["Intelligence Bonus"]
  Players["Jordy"]["Wisdom"] -= Equipment[equippedItem]["Wisdom Bonus"]
  Players["Jordy"]["Luck"] -= Equipment[equippedItem]["Luck Bonus"]

  with open("data.json", "w") as file:
    json.dump(source, file, indent=4)

def equipItem(item):
  with open("data.json") as file:
    source = json.load(file)
    Equipment = source["Equipment"]["Weapon"]
    Players = source["Players"]["Registered"]

  if item in Equipment:
    for nested_key, nested_val in Equipment.items():
      if nested_key == item:
        equipment = item
    if equipment != Players["Jordy"]["Weapon"]:
      if canEquipItem(equipment) == True:
        resetStats(Players["Jordy"]["Weapon"])
        recalculateStats(item)
        return f"{equipment} successfully equipped!"

      else:
        return canEquipItem(item)
    else:
      return f"You already have {equipment} equipped!"
  else:
    return "Unknown Item"

def recalculateStats(item):
  # Receive UserID from equipItem, then use it to change stats according to the equipped weapon's stat bonus
  with open("data.json", "r") as file:
    source = json.load(file)
    Equipment = source["Equipment"]["Weapon"]
    Player = source["Players"]["Registered"]

  Player["Jordy"]["Weapon"] = item
  Player["Jordy"]["Attack"] += Equipment[item]["Attack Power"]
  Player["Jordy"]["Strength"] += Equipment[item]["Strength Bonus"]
  Player["Jordy"]["Agility"] += Equipment[item]["Agility Bonus"]
  Player["Jordy"]["Intelligence"] += Equipment[item]["Intelligence Bonus"]
  Player["Jordy"]["Wisdom"] += Equipment[item]["Wisdom Bonus"]
  Player["Jordy"]["Luck"] += Equipment[item]["Luck Bonus"]

  with open("data.json", "w") as file:
    json.dump(source, file, indent=4)

def levelUp():
  with open("data.json", "r") as file:
    source = json.load(file)
  Players = source["Players"]["Registered"]
  requiredEXP = CostToLevel[Players["Jordy"]["Level"]]
  # check if the user is able to level up, if so change all stats by 2 and return True
  if Players["Jordy"]["EXP"] >= requiredEXP:
    Players["Jordy"]["Level"] += 1
    Players["Jordy"]["EXP"] -= requiredEXP
    Players["Jordy"]["Health"] += 2
    Players["Jordy"]["Attack"] += 2
    Players["Jordy"]["Strength"] += 2
    Players["Jordy"]["Agility"] += 2
    Players["Jordy"]["Intelligence"] += 2
    Players["Jordy"]["Wisdom"] += 2
    Players["Jordy"]["Luck"] += 2

    print(Players["Jordy"]["Level"])
    print(Players["Jordy"]["EXP"])
    with open("data.json", "w") as file:
      json.dump(source, file, indent=4)
      
    return True
  else:
    return False

def showStats():
  # loops to print all the information in a player's file
  with open("data.json", "r") as file:
    source = json.load(file)
  Players = source["Players"]["Registered"]
  response = []
  
  if levelUp():
    with open("data.json", "r") as file:
      source = json.load(file)
    newLevel = source["Players"]["Registered"]["Jordy"]["Level"]
    print(newLevel)
    print("Level up!")
    response.append(f"Congratulations, you've leveled up to level {newLevel}!\nAll your stats have risen by 2!\n")
  else:
    print("Nog niet level up!")
    pass
  
  with open("data.json", "r") as file:
    source = json.load(file)
  Players = source["Players"]["Registered"]
  for number, players in Players.items():
    for stats, values in players.items():
      response.append(f"{stats}: {values}")
      format_response = '\n'.join(response)
      
  with open("data.json", "w") as file:
    json.dump(source, file, indent=4)
    
  return format_response

def inspectEnemy():
  with open("data.json", "r") as file:
    source = json.load(file)
    Enemy = source["Enemies"]
  response = ["Your opponent is: Weak Goblin"]
  for number, race in Enemy.items():
    for enemy, attributes in race.items():
      for stats, values in attributes.items():
        response.append(f"{stats}: {values}")
        format_response = '\n'.join(response)
  return format_response

def canEquipItem(item):
  with open("data.json", "r") as file:
    source = json.load(file)
    Equipment = source["Equipment"]["Weapon"]
    Players = source["Players"]["Registered"]
  # Receive item and UserID from equipItem, to check if item can actually be wielded by the user, print an error "You cannot equip this yet!" if return false
  levelPlayer = Players["Jordy"]["Level"]
  reqLevelItem = Equipment[item]["Level Requirement"]
  # If player level is LOWER than required item level, show error message and return False, else return True
  if levelPlayer < reqLevelItem:
    return f"You can not equip {item} yet! You have to be level {reqLevelItem}, not level {levelPlayer}"
  else:
    return True

def calculateDamage(opponent):
  with open("data.json", "r") as file:
    source = json.load(file)
    Enemy = source["Enemies"]
    Players = source["Players"]["Registered"]
  # damage is a random number between 0 and max hit from player attack
  EnemyTarget = Enemy["Goblin"]["Weak Goblin"]
  Player = Players["Jordy"]
  if opponent == "Enemy":

    if calculateHit("Enemy"):
      damage = randint(0, Player["Attack"])
      enemyDamage = randint(0, EnemyTarget["Attack"])
      EnemyTarget["Health"] -= damage

      if EnemyTarget["Health"] <= 0:
        exp = randint(1, 30)
        with open("data.json", "w") as file:
          Player["EXP"] += exp
          enemyHP = 0
          EnemyTarget["Health"] = 0
          json.dump(source, file, indent=4)
        return f"You deal: {damage} damage! Weak Goblin has {enemyHP} HP remaining.\nWeak Goblin has been defeated! You have gained {exp} EXP!"
      else:
        enemyHP = EnemyTarget = Enemy["Goblin"]["Weak Goblin"]["Health"]
        if calculateHit("Player"):
          with open("data.json", "w") as file:
            Players["Jordy"]["Health"] -= enemyDamage
            if Players["Jordy"]["Health"] <= 0:
              Players["Jordy"]["Health"] = 0
            playerHP = Players["Jordy"]["Health"]
            json.dump(source, file, indent=4)

          if playerHP <= 0:
            return f"Weak Goblin deals {enemyDamage} damage!\nYou died!"
          else:
            return f"You deal: {damage} damage! Weak Goblin has {enemyHP} HP remaining.\nWeak Goblin deals {enemyDamage} damage! You have {playerHP} HP remaining!"

        else:
          return f"You deal: {damage} damage! Weak Goblin has {enemyHP} HP remaining.\nWeak Goblin missed!"
    else:
      enemyHP = EnemyTarget["Health"]
      #if calculateHit returns True (the enemy hits), grab a random integer between 0 and the enemy's 'max hit', proceed to calculate the remaining hit points and write this into the data.json for synchronization
      if calculateHit("Player"):
        enemyDamage = randint(0, EnemyTarget["Attack"])
        with open("data.json", "w") as file:
          enemyHP = EnemyTarget["Health"]
          Players["Jordy"]["Health"] -= enemyDamage
          playerHP = Players["Jordy"]["Health"]
          json.dump(source, file, indent=4)
          
        if playerHP <= 0:
          return f"Weak Goblin deals {enemyDamage} damage!\nYou died!"
        else:
          return f"You missed!\nWeak Goblin deals {enemyDamage} damage! You have {playerHP} HP remaining!"
          
      else:
        return f"You missed! Weak Goblin has {enemyHP} HP remaining.\nWeak Goblin missed!"
        
  else:
    enemyHP = EnemyTarget["Health"]
    #if calculateHit returns True (the enemy hits), grab a random integer between 0 and the enemy's 'max hit', proceed to calculate the remaining hit points and write this into the data.json for synchronization
    if calculateHit("Player"):
      enemyDamage = randint(0, EnemyTarget["Attack"])
      with open("data.json", "w") as file:
        enemyHP = EnemyTarget["Health"]
        Players["Jordy"]["Health"] -= enemyDamage
        playerHP = Players["Jordy"]["Health"]
        json.dump(source, file, indent=4)

      if playerHP <= 0:
        return f"Weak Goblin deals {enemyDamage} damage!\nYou died!"
      else:
        return f"You missed!\nWeak Goblin deals {enemyDamage} damage! You have {playerHP} HP remaining!"

    else:
      return f"You missed! Weak Goblin has {enemyHP} HP remaining.\nWeak Goblin missed!"

def calculateHit(opponent):
  #grabbing the data from "data.json" for use in calculations
  with open("data.json", "r") as file:
    source = json.load(file)
    Enemy = source["Enemies"]
    Players = source["Players"]["Registered"]
  EnemyTarget = Enemy["Goblin"]["Weak Goblin"]
  Player = Players["Jordy"]
  #checks to see which opponent is currently being targeted, if the opponent is "Enemy" then calculate playerHitChance, if the opponent is "Player" then calculate enemyHitChance
  if opponent == "Enemy":
    #takes a random int between 0 and player agility, which must be higher than the enemy's agility /2
    if randint(0, Player["Agility"]) > randint(0, EnemyTarget["Agility"]) / 3:
      return True
    else:
      return False
  elif opponent == "Player":
    if randint(0, EnemyTarget["Agility"]) > randint(0, Player["Agility"]) / 3:
      return True
    else:
      return False

def heal():
  #Create a function that allows for the healing of Player Health when needed, maybe replace for Health Potion use case later
  with open("data.json") as file:
    source = json.load(file)
    Player = source["Players"]["Registered"]
  Player["Jordy"]["Health"] = 10

  with open("data.json", "w") as file:
    json.dump(source, file, indent=4)

  return "Your Health has been restored!"

def fight():
  #Function to handle fighting, opening the .json file and selecting an enemy, checking if said enemy is still alive, if yes, continue with calculation, if not set Enemy health to 5, add this to the .json and proceed to fight again.
  with open("data.json") as file:
    source = json.load(file)
    Enemy = source["Enemies"]["Goblin"]["Weak Goblin"]
  if Enemy["Health"] <= 0:
    Enemy["Health"] = 5
    with open("data.json", "w") as file:
      json.dump(source, file, indent=4)
    if calculateHit("Enemy"):
      return calculateDamage("Enemy")
    else:
      return calculateDamage("Player")
  if calculateHit("Enemy"):
    return calculateDamage("Enemy")
  else:
    return calculateDamage("Player")

@reply_to_self(client, _USERNAME)
def send_message(message):

  if str(message.author.id) == _USERNAME:
    if str(message.content) == "$Stats":
      return showStats()
    #If $Equip (item) is shown in the chat, create a new variable called var, split the message every space and stop after the first split, proceed to grab the remaining list and convert it to a string
    if "$Equip" in str(message.content):
      var = message.content.split(" ", 1)[1:]
      item = " ".join(str(x) for x in var)
      return equipItem(item)
    # if the command is $Fight, call for the fight() function
    if "$Fight" in str(message.content):
      return fight()
    # if the command is $Inspect, call the inspectEnemy() function and return the list of data being printed ()
    if "$Inspect" in str(message.content):
      return inspectEnemy()

    if "$Heal" in str(message.content):
      return heal()

    else:
      return "Unknown Command"

  else:
    return ("Unknown User")


try:
  print("Lets go")
  client.run(TOKEN)
except Exception as e:
  print(e)
  os.system("kill 1")
