
from constants import game_settings as gs
from classes import entity as ent
from classes import collision as col


class Npc(ent.Entity):

    nb_npc = 0
    def __init__(self,npc_type, npc_id, parametre):
        """
            * parametre =  [position, taille, type_deplacement, vie, attaque]
        """
        Npc.nb_npc +=1  # increments npc number
        super(Npc, self).__init__(npc_type, npc_id, parametre)  # superclass
        # entity settings for NPCs
        x, y = parametre[0]  # Spawn position
        x += gs.map.x_camera
        y += gs.map.y_camera
        self.position = [x, y]
        self.taille = parametre[1]
        self.type_deplacement = parametre[2]
        self.hitbox = col.Hitbox("Npc")  # NPC collisions
