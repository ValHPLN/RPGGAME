import pygame as pg

from classes import player
from constants import game_settings as gs


class Inventory:
    def __init__(self, player, totalSlots, cols, rows):
        self.totalSlots = totalSlots
        self.rows = rows
        self.cols = cols
        self.inventory_slots = []
        self.display_inventory = False
        self.player = player
        self.appendSlots()

        self.movingitem = None
        self.movingitemslot = None

    def appendSlots(self):
        while len(self.inventory_slots) != self.totalSlots:
            for x in range(gs.WIDTH // 2 - ((gs.INVTILESIZE + 2) * self.cols) // 2, (gs.WIDTH // 2 + ((gs.INVTILESIZE + 2) * self.cols) // 2), gs.INVTILESIZE + 2):
                for y in range(gs.HEIGHT, (gs.HEIGHT + gs.INVTILESIZE * self.rows), gs.INVTILESIZE + 2):
                    self.inventory_slots.append(InventorySlot(x, y))

    def draw(self, screen):
        if self.display_inventory:
            for slot in self.inventory_slots:
                slot.draw(screen)
            for slot in self.inventory_slots:
                slot.drawItems(screen)

    def toggleInventory(self):
        self.display_inventory = not self.display_inventory

    def addItemInv(self, item, slot=None):
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

    def removeItemInv(self, item):
        for slot in self.inventory_slots:
            if slot.item == item:
                slot.item = None
                break

    def moveItem(self, screen):
        mousepos = pg.mouse.get_pos()
        for slot in self.inventory_slots:
            if slot.draw(screen).collidepoint(mousepos) and slot.item != None:
                slot.item.is_moving = True
                self.movingitem = slot.item
                self.movingitemslot = slot
                break

    def placeItem(self, screen):
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

    def checkSlot(self, screen, mousepos):
        for slot in self.inventory_slots:
            if isinstance(slot, InventorySlot):
                if slot.draw(screen).collidepoint(mousepos):
                    if isinstance(slot.item, Consumable):
                        self.useItem(slot.item)

    def useItem(self, item):
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
            screen.blit(self.image, (self.x + 20, self.y + 20))
        if self.item != None and self.item.is_moving:
            mousepos1 = pg.mouse.get_pos()
            self.image = pg.image.load(self.item.img).convert_alpha()
            screen.blit(self.image, (mousepos1[0] - 20, mousepos1[1] - 20))


class InventoryItem:
    def __init__(self, img, value):
        self.img = img
        self.value = value
        self.is_moving = False


class Consumable(InventoryItem):
    def __init__(self, img, value, hp_gain=0):
        InventoryItem.__init__(self, img, value)
        self.hp_gain = hp_gain

    def use(self, inv, target):
        inv.removeItemInv(self)
        gs.base_hp += 2
        print(gs.base_hp)




