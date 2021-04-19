import math
from random import uniform, random


# Calculate the damage of an attack. Takes an ability, the persona attacking, and the persona defending.
def damage(ability, char, target):
    status = False
    crit = False
    mod = 0

    if ability.mod == "ma":
        mod = char.ma
    elif ability.mod == "st":
        mod = char.st

    diff = (char.level - target.level)
    if diff > 1:
        level_mod = (.75 * (math.log(diff + 1))) + .25
    elif diff < -1:
        level_mod = (.75 * (1 / (math.log(diff * (-1) + 1)))) + .25
    else:
        level_mod = 1

    damage_diff = (mod - target.en)
    if damage_diff > 0:
        damage_mod = (math.log(damage_diff + 2))
    elif damage_diff < 0:
        damage_mod = (1 / (math.log(damage_diff * (-1) + 2)))
    else:
        damage_mod = 1

    luck_differance = char.lu - target.lu
    if luck_differance > 0:
        luck_mod = (.75 * (math.log(luck_differance + 2))) + .25
    elif luck_differance < 0:
        luck_mod = (.75 * (1 / (math.log(luck_differance * (-1) + 2)))) + .25
    else:
        luck_mod = 1

    status_chance = ability.status * luck_mod
    roll = random()
    if roll < status_chance:
        status = True

    crit_chance = ability.crit * luck_mod
    roll2 = random()
    if roll2 < crit_chance:
        crit = True
    print("crit_chance: " + str(crit_chance))
    print("status_chance: " + str(status_chance))
    crit_mod = 1
    if crit:
        crit_mod = 1.5
        print("CRIT!")
    if status:
        print("AILMENT!")
    print("\n")
    dmg = round((crit_mod* .25 * (damage_mod * ability.power * math.sqrt(math.log(char.level+1)) * uniform(0.95, 1.05))) - (target.armor/4))
    if crit:
        text = char.name + " CRITS! doing " + str(dmg) + " to " + target.name + " with " + ability.name
    else:
        text = char.name + " does " + str(dmg) + " with " + ability.name
    if status:
        text = text + " AND applies AILMENT!"
    print(char.name + " does " + str(dmg) + " with " + ability.name)

    return text


# Calculate the chance to hit of an attack.
def hit(ability, char, target):
    has_hit = False

    if ability.acc is True:
        print("acc: 100%")
        has_hit = True
        print(char.name + " hits " + target.name + " with " + ability.name)
        return has_hit

    diff = (char.ag - target.ag)
    if diff > 0:
        acc_mod = (.75 * (math.log(diff + 2))) + .25
    elif diff < 0:
        acc_mod = (.75 * (1 / (math.log(diff * (-1) + 2)))) + .25
    else:
        acc_mod = 1

    acc = ((ability.acc - (target.evade / 100)) * acc_mod)
    print("acc: " + str(acc))
    roll = random()
    if roll < acc:
        has_hit = True
        print(char.name + " hits " + target.name + " with " + ability.name)
    else:
        print(char.name + " misses " + target.name + "\n")

    return has_hit


def heal(ability, char):
    healed = round(ability.power * ((.25 * math.log(char.ma)) + 1) * uniform(0.95, 1.05))
    print(char.name + " used " + ability.name + " for " + str(healed) + " health\n")
