# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Damage_Calculator
import EXP_Calculator
import PySimpleGUI as sg


class Persona:
    def __init__(self, name, st, ma, en, ag, lu, level, armor, evade):
        self.name = name
        self.st = st
        self.ma = ma
        self.en = en
        self.ag = ag
        self.lu = lu
        self.level = level
        self.armor = armor
        self.evade = evade

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return self.name


class Ability:
    def __init__(self, name, mod, power, acc, status, crit, cost):
        self.name = name
        self.mod = mod
        self.power = power
        self.acc = acc
        self.status = status
        self.crit = crit
        self.cost = cost

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return self.name


Arse = Persona("Arsè",
               3,  # st
               6,  # ma
               9,  # en
               5,  # ag
               4,  # lu
               6,  # level
               47,  # armor
               10)  # evade

# +2 STR , +2 AGI
Moth = Persona("Moth",
               9,  # st
               1,  # ma
               8,  # en
               4,  # ag
               9,  # lu
               6,  # level
               47,  # armor
               10, )  # evade

Jormungandr = Persona("Jormungandr",
                      4,  # st
                      9,  # ma
                      6,  # en
                      5,  # ag
                      3,  # lu
                      6,  # level
                      47,  # armor
                      10)  # evade

Arthur = Persona("Arthur",
                 2,  # st
                 14,  # ma
                 1,  # en
                 7,  # ag
                 5,  # lu
                 6,  # level
                 45,  # armor
                 15)  # evade

# Knows cleave, cower and flee. Drops $30 and 30 exp. Has no affinities.
Money_Hand = Persona("Money Hand",
                     1,  # st
                     1,  # ma
                     1,  # en
                     30,  # ag
                     30,  # lu
                     5,  # level
                     0,  # armor
                     0)  # evade

# 56 Health. Strong to Elec and Bless. Weak to Gun. Ice and Curse Knows Dia and Kouha. EXP 4. Yen $1.
Pixie = Persona("Pixie",
                1,  # st
                3,  # ma
                3,  # en
                4,  # ag
                3,  # lu
                2,  # level
                0,  # armor
                0)  # evade

# 62 Health. Weak to Fire, Elec and Wind. Knows Lunge attack and Bufu. 4 exp. $1.
Cowardly_Maya = Persona("Cowardly Maya",
                        2,  # st
                        4,  # ma
                        3,  # en
                        3,  # ag
                        2,  # lu
                        2,  # level
                        0,  # armor
                        0)  # evade

# 75 HP. Weak to Gun, Ice and Wind. Drains Fire. Knows Agi. 4 EXP $1
Pyro_Jack = Persona("Pyro_Jack",
                    2,  # st
                    5,  # ma
                    3,  # en
                    1,  # ag
                    2,  # lu
                    2,  # level
                    0,  # armor
                    0)  # evade

# 95 Health. Strong vs Elec. Weak to Fire. Knows Pulinpa. 6 exp, $0.80
Mandrake = Persona("Mandrake",
                   4,  # st
                   3,  # ma
                   3,  # en
                   3,  # ag
                   3,  # lu
                   3,  # level
                   0,  # armor
                   0)  # evade

# 66 Health. Strong vs Fire, Ice, Elec and Wind. Weak to light. Knows Garu, Agi, Bufu and Zio. 6 exp, $1
Dark_Spell_Book = Persona("Dark Spell Book",
                          2,  # st
                          6,  # ma
                          3,  # en
                          2,  # ag
                          4,  # lu
                          3,  # level
                          0,  # armor
                          0)  # evade

# 67 Health. Strong vs Fire. Weak to Ice, Elec, Wind. Knows Cleave and Agi. 6 exp, $1.50
Merciless_Maya = Persona("Merciless Maya",
                         4,  # st
                         5,  # ma
                         3,  # en
                         2,  # ag
                         3,  # lu
                         3,  # level
                         0,  # armor
                         0)  # evade

# 54 Health. Strong to Elec, weak to Wind. Knows Cleave and Zio. 6 exp, $1.50
Muttering_Tiara = Persona("Muttering Tiara",
                          3,  # st
                          5,  # ma
                          3,  # en
                          2,  # ag
                          3,  # lu
                          3,  # level
                          0,  # armor
                          0)  # evade

# 62 Health, Weak to fire, strong to Ice.
# Knows Lunge, Bufu and Mabufu. $1.5, 8 exp
Magic_Hand = Persona("Magic Hand",
                     3,  # st
                     7,  # ma
                     4,  # en
                     3,  # ag
                     2,  # lu
                     4,  # level
                     0,  # armor
                     0)  # evade

# 62 Health, Weak to Wind, strong to Elec.
# Knows Lunge, Zio and Mazio. $1.5, 8 exp
Magic_Hand_Lightning = Persona("Magic Hand Lightning",
                               3,  # st
                               7,  # ma
                               4,  # en
                               3,  # ag
                               2,  # lu
                               4,  # level
                               0,  # armor
                               0)  # evade

# 66 Health. Drain Ice. Null Light, Weak to Dark. Knows Hama, Kouha and Mabufu.  8 exp, $2
Light_Spell_Book = Persona("Light Spell Book",
                           2,  # st
                           6,  # ma
                           4,  # en
                           3,  # ag
                           5,  # lu
                           4,  # level
                           0,  # armor
                           0)  # evade

# knows Single Shot, Garu and Dia. Weak to Ice, Strong to Wind
# 12 EXP, $2, 58 HP.
Obsessed_Cupid = Persona("Obsessed Cupid",
                         2,  # st
                         5,  # ma
                         3,  # en
                         7,  # ag
                         5,  # lu
                         5,  # level
                         0,  # armor
                         0)  # evade

# 73 Health, Strong vs Fire, Weak vs Ice and Elec
# Knows Lunge, Agi and Dia, 12 EXP, $1.4
Lying_Hablerie = Persona("Lying Hablerie",
                         5,  # st
                         5,  # ma
                         3,  # en
                         3,  # ag
                         3,  # lu
                         5,  # level
                         0,  # armor
                         0)  # evade

# 100 Health, Weak to Fire, Strong to Gun, Null Ice
# Knows Lunge, Bufu and Pulinpa, 12 EXP, $1.5
Laughing_Table = Persona("Laughing Table",
                         5,  # st
                         5,  # ma
                         4,  # en
                         3,  # ag
                         3,  # lu
                         5,  # level
                         0,  # armor
                         0)  # evade

# knows Cleave, Garu and Magaru. Drain Fire. Null Wind, Light and Dark
# 20 EXP, $2 Yen. 150 HP. Weak to Gun.
Venus_Eagle = Persona("Venus Eagle",
                      8,  # st
                      5,  # ma
                      4,  # en
                      12,  # ag
                      5,  # lu
                      5,  # level
                      0,  # armor
                      0)  # evade

# knows Evil Touch, Eiha and Tarunda.
# 14 EXP, $2. 103 HP
Incubus = Persona("Incubus",
                  5,  # st
                  6,  # ma
                  6,  # en
                  7,  # ag
                  4,  # lu
                  5,  # level
                  0,  # armor
                  0)  # evade

# knows Lunge, Zio, Mazio.
# 20 EXP, $3. 150 HP. Weak to Fire and Ice. Strong to Elc
Trance_Twins = Persona("Trance Twins",
                       4,  # st
                       8,  # ma
                       5,  # en
                       4,  # ag
                       4,  # lu
                       6,  # level
                       0,  # armor
                       0)  # evade

# knows Garu, Lunge and Summon Kelpie.
# 22 EXP, $2.5. 128 HP. Strong to Ice and Wind. Weak to Elec
Kelpie = Persona("Kelpie",
                 6,  # st
                 5,  # ma
                 5,  # en
                 8,  # ag
                 6,  # lu
                 6,  # level
                 0,  # armor
                 0)  # evade

# 130 HP Knows Psi, Ominous_Words, dia (self only)
# 20 EXP, $3 weak to nuke, Null psi, resist bless and dark.
Witch = Persona("Witch",
                2,  # st
                8,  # ma
                5,  # en
                4,  # ag
                8,  # lu
                6,  # level
                0,  # armor
                0)  # evade

Mosquito = Persona("Mosquito",
                   8,  # st
                   4,  # ma
                   4,  # en
                   10,  # ag
                   7,  # lu
                   7,  # level
                   0,  # armor
                   0)  # evade

Black_Raven = Persona("Black Raven",
                      8,  # st
                      4,  # ma
                      4,  # en
                      5,  # ag
                      3,  # lu
                      7,  # level
                      0,  # armor
                      0)  # evade

Succubus = Persona("Succubus",
                   5,  # st
                   10,  # ma
                   6,  # en
                   9,  # ag
                   8,  # lu
                   7,  # level
                   0,  # armor
                   0)  # evade

Death_Worm = Persona("Death Worm",
                     9,  # st
                     8,  # ma
                     11,  # en
                     4,  # ag
                     4,  # lu
                     8,  # level
                     0,  # armor
                     0)  # evade

# 125 Health. Strong vs Elec. Weak to Wind. Knows Cleave, Zio and Mazio
Frivolous_Maya = Persona("Frivolous Maya",
                         8,  # st
                         7,  # ma
                         7,  # en
                         12,  # ag
                         7,  # lu
                         11,  # level
                         0,  # armor
                         0)  # evade

# knows Poison Skewer,Eiha, Mudo, Evil Smile
Shadow_Phil = Persona("Shadow Phil",
                      16,  # st
                      7,  # ma
                      8,  # en
                      6,  # ag
                      10,  # lu
                      11,  # level
                      0,  # armor
                      0)  # evade

Agi = Ability("Agi", "ma", 80, .98, .1, 0, 4)
Maragi = Ability("Maragi", "ma", 80, .95, .1, 0, 10)

Bufu = Ability("Bufu", "ma", 80, .98, .1, 0, 4)
Mabufu = Ability("Mabufu", "ma", 80, .95, .1, 0, 10)

Zio = Ability("Zio", "ma", 80, .98, .1, 0, 4)
Mazio = Ability("Mazio", "ma", 80, .95, .1, 0, 10)
Zionga = Ability("Zionga", "ma", 200, .98, .1, 0, 8)

Garu = Ability("Garu", "ma", 80, .98, 0, 0, 4)
Magaru = Ability("Magaru", "ma", 80, .95, 0, 0, 10)

Psi = Ability("Psi", "ma", 80, .98, 0, 0, 4)
Mapsi = Ability("Mapsi", "ma", 80, .95, 0, 0, 10)

Frei = Ability("Frei", "ma", 80, .98, 0, 0, 4)
Freila = Ability("Freila", "ma", 80, .95, 0, 0, 10)

Kouha = Ability("Kouha", "ma", 100, .98, 0, 0, 4)
Makouha = Ability("Makouha", "ma", 100, .95, 0, 0, 10)
Hama = Ability("Hama", "ma", 0, True, .4, 0, 8)
Mahama = Ability("Mahama", "ma", 0, True, .3, 0, 8)

Eiha = Ability("Eiha", "ma", 100, .98, 0, 0, 4)
Maeiha = Ability("Maeiha", "ma", 100, .95, 0, 0, 10)
Mudo = Ability("Mudo", "ma", 0, True, .4, 0, 8)
Mamudo = Ability("Mamudo", "ma", 0, True, .3, 0, 18)

Dia = Ability("Dia", "ma", 30, True, 0, 0, 3)
Diarama = Ability("Diarama", "ma", 80, True, 0, 0, 8)

Media = Ability("Media", "ma", 25, True, 0, 0, 7)
Mediarama = Ability("Mediarama", "ma", 70, True, 0, 0, 7)

Punch = Ability("Punch", "st", 20, .9, 0, .2, "0")
Minecraft_Sword = Ability("Sword", "st", 49, .96, 0, .2, "0")
Wand = Ability("Wand", "st", 15, .95, 0, .2, "0")
Fake_Mace = Ability("Fake_Nunchuk", "st", 53, .92, 0, .2, "0")
Baseball_Bat = Ability("Baseball_Bat", "st", 51, .85, 0, .2, "0")

Cleave = Ability("Cleave", "st", 130, 1, 0, .2, "5%")
Lunge = Ability("Lunge", "st", 140, .85, 0, .2, "8%")
Poison_Skewer = Ability("Poison Skewer", "st", 120, .9, .5, .05, "8%")

Gale_Slash = Ability("Gale Slash", "st", 160, .85, 0, .05, "12%")

Single_Shot = Ability("Single Shot", "st", 150, .9, 0, .25, "8%")

Evil_Touch = Ability("Evil Touch", "ma", 0, True, .75, 0, 5)
Pulinpa = Ability("Pulinpa", "ma", 0, True, .75, 0, 5)
Ominous_Words = Ability("Ominous Words", "ma", 0, True, .75, 0, 5)
Taunt = Ability("Taunt", "ma", 0, True, .75, 0, 5)
Marin_Karin = Ability("Marin Karin", "ma", 0, True, .75, 0, 5)
Dazzler = Ability("Dazzler", "ma", 0, True, .75, 0, 5)
Makajama = Ability("Makajama", "ma", 0, True, .75, 0, 5)
Dormina = Ability("Dormina", "ma", 0, True, .75, 0, 5)

Evil_Smile = Ability("Evil Smile", "ma", 0, True, .45, 0, 10)


def attack(ability, user, target):
    if Damage_Calculator.hit(ability, user, target):
        return Damage_Calculator.damage(ability, user, target)
    else:
        return user.name + " missed " + target.name + " with " + ability.name


def ui():
    personas = (Moth, Arse, Jormungandr, Arthur, Magic_Hand, Incubus, Kelpie, Succubus, Death_Worm, Frivolous_Maya)
    abilities = (Agi, Maragi, Bufu, Mabufu, Zio, Mazio, Zionga, Garu, Magaru, Eiha, Cleave, Gale_Slash)

    layout = [
        [sg.Combo(personas, size=(30, 5), enable_events=True, key='Persona1')],
        [sg.Combo(personas, size=(30, 5), enable_events=True, key='Persona2')],
        [sg.Combo(abilities, size=(30, 5), enable_events=True, key='Ability')],
        [sg.Button("Attack")],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Button("END")]
    ]

    window = sg.Window("Purse Owners", layout, finalize=True, margins=(100, 40))
    combo = window['Persona1']
    combo.bind("<Enter>", "ENTER-")

    while True:

        event, values = window.read()
        print(event, values)

        if event == "END" or event == sg.WIN_CLOSED:
            break
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-COMBO-ENTER-":
            combo.Widget.event_generate('<Button-1>')
        if event == "Attack":
            print(values["Persona1"].name)
            print(values["Ability"].name)
            window['-OUTPUT-'].update(attack(values["Ability"], values["Persona1"], values["Persona2"]))

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ui()
    # EXP_Calculator.chart()

    # attack(Maeiha, Arse, Lying_Hablerie)
    # attack(Maeiha, Arse, Lying_Hablerie)
    # attack(Maeiha, Arse, Obsessed_Cupid)
    # attack(Maeiha, Arse, Cowardly_Maya)
    # attack(Maeiha, Arse, Cowardly_Maya)
    # attack(Maeiha, Arse, Kelpie)
    # attack(Maeiha, Arse, Kelpie2)

    # attack(Eiha, Arse, Death_Worm)
    # attack(Cleave, Moth, Eligor)
    # attack(Kouha, Moth, Dark_Spell_Book)
    # attack(Zio, Arthur, Black_Raven)
    # attack(Bufu, Jormungandr, Death_Worm)
    # attack(Pulinpa, Jormungandr, Venus_Eagle)
    # attack(Mudo, Moth, Kelpie)
    # attack(Single_Shot, Arse, Succubus)

    # attack(Mazio, Arthur, Death_Worm)
    # attack(Mazio, Arthur, Death_Worm)
    # attack(Mazio, Arthur, Succubus)
    # attack(Mazio, Arthur, Succubus)

    # attack(Gale_Slash, Moth, Death_Worm)
    # attack(Gale_Slash, Moth, Death_Worm)
    # attack(Gale_Slash, Moth, Succubus)

    # attack(Fake_Mace, Jormungandr, Death_Worm)
    # attack(Fake_Mace, Arse, Death_Worm)
    # attack(Minecraft_Sword, Moth, Death_Worm)
    # attack(Wand, Arthur, Death_Worm)

    # attack(Lunge, Mosquito, Moth)
    # attack(Magaru, Venus_Eagle, Arse)
    # attack(Magaru, Venus_Eagle, Moth)
    # attack(Magaru, Venus_Eagle, Arthur)
    # attack(Magaru, Venus_Eagle, Jormungandr)
    # attack(Marin_Karin, Succubus, Moth)
    # attack(Eiha, Death_Worm, Arthur)
    # attack(Evil_Touch, Death_Worm, Arse)

    # attack(Poison_Skewer, Shadow_Phil, Moth)
    # attack(Evil_Smile, Shadow_Phil, Arse)
    # attack(Evil_Smile, Shadow_Phil, Moth)
    # attack(Evil_Smile, Shadow_Phil, Arthur)
    # attack(Evil_Smile, Shadow_Phil, Jormungandr)

    # Damage_Calculator.heal(Dia, Moth)
    # Damage_Calculator.heal(Dia, Jormungandr)
    # Damage_Calculator.heal(Dia, Arse)
    # Damage_Calculator.heal(Media, Jormungandr)
    # Damage_Calculator.heal(Media, Jormungandr)
    # Damage_Calculator.heal(Media, Jormungandr)
    # Damage_Calculator.heal(Media, Jormungandr)
