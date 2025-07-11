from code.Ally import Ally
from code.Player import Player

from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, Ally)):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        if isinstance(ent1, Player) and isinstance(ent2, Ally):
            valid_interaction = True
        if isinstance(ent1, Ally) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # mesmo que if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(entity: Entity, entity_list: list[Entity]):
        if isinstance(entity, Enemy):
            if entity.last_dmg == 'Player1':
                for ent in entity_list:
                    if ent.name == 'Player1':
                        ent.score -= entity.score
            elif entity.last_dmg == 'Player2':
                for ent in entity_list:
                    if ent.name == 'Player2':
                        ent.score -= entity.score

        elif isinstance(entity, Ally):
            if entity.last_dmg == 'Player1':
                for ent in entity_list:
                    if ent.name == 'Player1':
                        ent.score += entity.score
                        ent.health += entity.damage
            elif entity.last_dmg == 'Player2':
                for ent in entity_list:
                    if ent.name == 'Player2':
                        ent.score += entity.score
                        ent.health += entity.damage

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        to_remove = []
        for ent in entity_list:
            if ent is not None and hasattr(ent, "health") and ent.health <= 0:
                if isinstance(ent, (Enemy, Ally)):
                    EntityMediator.__give_score(ent, entity_list)
                to_remove.append(ent)
        for ent in to_remove:
            entity_list.remove(ent)
