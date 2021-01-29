from classes.inventory import Consumable, Quest

#stores items images and category as variables (easier to add to inventory)

hp_potion = Consumable('img/objects/coffee.png', 2)
glasses = Quest('img/objects/glasses.png', 2)
cable = Quest('img/objects/cable2.png', 2)
coin = Quest('img/objects/coin.png', 2)

#used for quests (if item = 1, means you have one in your inventory)
glassesNb = 0
coinNb = 0
cableNb = 0