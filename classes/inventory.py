import pygame as pg

from classes import player
from constants import game_settings as gs
from constants import player_settings as ps


class Inventory: #sets up inventory class that can be updated if we add more items later on
    def __init__(self, player, totalSlots, cols, rows):
        self.totalSlots = totalSlots
        self.rows = rows
        self.cols = cols
        self.inventory_slots = [] #stores slots
        self.display_inventory = False
        self.player = player
        self.appendSlots()

        self.movingitem = None
        self.movingitemslot = None

    def appendSlots(self): #complicated bit but basically sets up position of the slots
        while len(self.inventory_slots) != self.totalSlots:
            for x in range(gs.WIDTH // 2 - ((gs.INVTILESIZE + 2) * self.cols) // 2, (gs.WIDTH // 2 + ((gs.INVTILESIZE + 2) * self.cols) // 2), gs.INVTILESIZE + 2):
                for y in range(gs.HEIGHT, (gs.HEIGHT + gs.INVTILESIZE * self.rows), gs.INVTILESIZE + 2):
                    self.inventory_slots.append(InventorySlot(x, y))

    def draw(self, screen): #calls functions to draw slots and the items inside
        if self.display_inventory:
            for slot in self.inventory_slots:
                slot.draw(screen)
            for slot in self.inventory_slots:
                slot.drawItems(screen)

    def toggleInventory(self):
        self.display_inventory = not self.display_inventory

    def addItemInv(self, item, slot=None): #checks if there's an empty slot in list, then appends item in one of them
        if slot == None:
            for slots in self.inventory_slots:
                if slots.item == None:
                    slots.item = item
                    break
        if slot != None:
            if slot.item != None:
                self.movingitemslot.item = slot.item
                slot.item = item
            else:
                slot.item = item

    def removeItemInv(self, item): #sets slot state to none according to item ID
        for slot in self.inventory_slots:
            if slot.item == item:
                slot.item = None
                break

    def moveItem(self, screen): #checks collision between mouse and item, allows us to move the item in the inventory
        mousepos = pg.mouse.get_pos()
        for slot in self.inventory_slots:
            if slot.draw(screen).collidepoint(mousepos) and slot.item != None:
                slot.item.is_moving = True
                self.movingitem = slot.item
                self.movingitemslot = slot
                break

    def placeItem(self, screen): #checks position of the slot and the mouse, if we're holding an item above a slot, drops it in the slot
        mousepos = pg.mouse.get_pos()
        for slot in self.inventory_slots:
            if slot.draw(screen).collidepoint(mousepos) and self.movingitem != None:
                if isinstance(slot, InventorySlot):
                    self.removeItemInv(self.movingitem)
                    self.addItemInv(self.movingitem, slot)
                    break
        if self.movingitem != None:
            self.movingitem.is_moving = False
            self.movingitem = None
            self.movingitemslot = None

    def checkSlot(self, screen, mousepos): #checks the category of item, if it's a consumable, it can be used
        for slot in self.inventory_slots:
            if isinstance(slot, InventorySlot):
                if slot.draw(screen).collidepoint(mousepos):
                    if isinstance(slot.item, Consumable):
                        self.useItem(slot.item)

    def useItem(self, item): #use item (only consumables can be used so far)
        if isinstance(item, Consumable):
            item.use(self, self.player)


class InventorySlot:
    def __init__(self, x, y):
        self.x = x
        self.y = y-400
        self.item = None

    def draw(self, screen):
        return pg.draw.rect(screen, gs.LIGHTGREY, (self.x, self.y, gs.INVTILESIZE, gs.INVTILESIZE))

    def drawItems(self, screen):
        if self.item != None and not self.item.is_moving:
            self.image = pg.image.load(self.item.img).convert_alpha()
            screen.blit(self.image, (self.x + 10, self.y + 10))
        if self.item != None and self.item.is_moving:
            mousepos1 = pg.mouse.get_pos()
            self.image = pg.image.load(self.item.img).convert_alpha()
            screen.blit(self.image, (mousepos1[0] - 20, mousepos1[1] - 20))


class InventoryItem: #settings for inventory items, value is currently unused but might be if we add a shop
    def __init__(self, img, value):
        self.img = img
        self.value = value
        self.is_moving = False


class Consumable(InventoryItem):
    def __init__(self, img, value):
        InventoryItem.__init__(self, img, value)

    def use(self, inv, target): #currently, restores HP when you use a consumable, must be modified to access class values and allow other consumables wih differents effets
        inv.removeItemInv(self)
        if gs.base_hp < 25:
            gs.base_hp = gs.max_hp

class Quest(InventoryItem): # to define quest objects
    def __init__(self, img, value):
        InventoryItem.__init__(self, img, value)





