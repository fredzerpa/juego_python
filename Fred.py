class Character:
    def __init__(self, name='Anonymous', sex='Masculino', race='Guerrero', hp=100, attack=10, defense=5):
        self.name = name
        self.sex = sex
        self.race = race
        self.health = hp
        self.attack_points = attack
        self.defense_points = defense
        self.skills = []
        print(f"\nSoy {self.name} el {self.race}, me adentrare en esta aventura contigo!\n")

    def set_health_points(self, points):
        self.health = points

    def set_attack_points(self, points):
        self.attack_points = points

    def attack(self):
        return self.attack_points

    def set_def_points(self, points):
        self.defense_points = points

    def set_skills(self, skill):
        self.skills.append(skill)

    def show_status(self):
        print()
        print('Nombre: ', self.name)
        print('Sexo: ', self.sex)
        print('Raza: ', self.race)
        print('HP: ', self.health)
        print('Ataque: ', self.attack_points)
        print('Defensa: ', self.defense_points)
        show_skills = "Habilidades: "
        for skill in self.skills:
            show_skills += f" {skill['name']} ({skill['damage_points']})"
        print(show_skills)
        print()


class Monster:
    def __init__(self, name, race, hp=50, attack=8, defense=5):
        self.name = name
        self.race = race
        self.health = hp
        self.attack_points = attack
        self.defense_points = defense

    def set_health_points(self, points):
        self.health = points

    def set_attack_points(self, points):
        self.attack_points = points

    def attack(self):
        return self.attack_points

    def set_def_points(self, points):
        self.defense_points = points

    def greet(self):
        print("ROOOOOOAARR!!!")


valid_option_between_nums = lambda op, nums: op in range(nums[0], nums[1])


def new_character(class_creation):
    print("Para comenzar con una nueva aventura escoja su clase.")
    print("1. Guerrero")
    print("     Ataque -> Medio, Defensa -> Alta, Vida -> Alta")
    print("2. Mago")
    print("     Ataque -> Alto, Defensa -> Baja, Vida -> Medio")
    print("3. Arquero")
    print("     Ataque -> Medio, Defensa -> Medio, Vida -> Alta")

    is_valid = False

    while not is_valid:
        race = input("Numero de la Clase: ")
        if race.isnumeric() and valid_option_between_nums(int(race), [1, 4]):
            is_valid = True
            race = "Guerrero" if int(race) == 1 else "Mago" if int(race) == 2 else "Arquero"
        else:
            print("\"Ingrese un valor valido [1  2  3]\"")

    name = input("Nombre: ").capitalize()

    is_valid = False
    while not is_valid:
        print("Sexo: \n 1. Masculino \n 2. Femenino")
        sex = input("Sexo: ")
        if sex.isnumeric() and valid_option_between_nums(int(sex), [1, 3]):
            is_valid = True
            sex = "Masculino" if int(sex) == 1 else "Femenino"
        else:
            print("\"Ingrese un valor valido [1  2]\"")

    if race == "Guerrero":
        char = class_creation(name, sex, race)
        char.set_skills(
            {'name': 'Corte', 'damage_points': 12}
        )
    elif race == "Mago":
        char = class_creation(name, sex, race, 80, 15, 2)
        char.set_skills(
            {'name': 'Bola de fuego', 'damage_points': 18}
        )
    else:
        char = class_creation(name, sex, race, 90, 12, 4)
        char.set_skills(
            {'name': 'Flecha afilada', 'damage_points': 15}
        )

    return char


def menu():
    is_valid = False
    while not is_valid:
        print("Escoja una opcion para continuar:")
        print(" 1.  Crear nuevo personaje.")
        print(" 2.  Estado del personaje.")
        print(" 3.  Atacar nuevo monstruo.")
        print(" 4.  Salir.")
        op = input("Opcion: ")
        if valid_option_between_nums(int(op), [1, 5]):
            is_valid = True
            return int(op) if valid_option_between_nums(int(op), [1, 4]) else exit()
        else:
            print("\"Escoja una opcion valida [1 2 3 4]\"")


def att_and_run_menu():
    is_valid = False
    while not is_valid:
        print("Escoja una accion para continuar:")
        print(" 1.  Atacar.")
        print(" 2.  Habilidades.")
        print(" 3.  Escapar.")
        op = input("Accion: ")
        if valid_option_between_nums(int(op), [1, 4]):
            # is_valid = True
            return int(op)
        else:
            print("\"Escoja una opcion valida [1 2 3]\"")


def select_skill(skills):
    for skill in skills:
        is_valid = False
        while not is_valid:
            print("Escoja una accion para continuar:")
            for data in skill.values():
                print(f" 1.  {data}.")
                print(" 2.  Regresar.")
                op = input("Accion: ")
                if valid_option_between_nums(int(op), [1, 2]):
                    is_valid = True
                    return int(op)
                else:
                    print("\"Escoja una opcion valida [1]\"")


def damage_dealt(attack_points, defense_points):
    damage = (attack_points - defense_points) if attack_points > defense_points else 0
    return damage


print()
print("Bienvenido a una Nueva Aventura!")
print()
adventurer = new_character(Character)
while True:
    selected_menu = menu()
    if selected_menu == 1:  # New Character
        adventurer = new_character(Character)
        print()
    elif selected_menu == 2:  # Show Stats
        adventurer.show_status()
    else:  # Monster Subjugation
        new_monster = Monster('Arachnee', 'Spider')
        print()
        new_monster.greet()
        print()
        print(f"Ha aparecido un {new_monster.name}!")
        print()
        has_run = False
        while new_monster.health > 0 and not has_run:
            selected_action = att_and_run_menu()
            print()
            if selected_action == 1:
                damage_points = damage_dealt(adventurer.attack_points, new_monster.defense_points)
                hp_left = new_monster.health - damage_points
                new_monster.set_health_points(hp_left)
                print(f"Has realizado {damage_points} de daño al monstruo! "
                      f"\n   {new_monster.name} => HP: {new_monster.health}")
                print()
                damage_points = damage_dealt(new_monster.attack_points, adventurer.defense_points)
                hp_left = adventurer.health - damage_points
                adventurer.set_health_points(hp_left)
                print(f"{new_monster.name} te ha atacado! Te ha quitado "
                      f"{damage_points} de Vida."
                      f"\n  {adventurer.name} => HP: {adventurer.health}")
                print()

            elif selected_action == 2:
                selected_skill = select_skill(adventurer.skills)
                skill_damage = adventurer.skills[selected_skill - 1]['damage_points']
                damage_points = damage_dealt(skill_damage, new_monster.defense_points)
                hp_left = new_monster.health - damage_points
                new_monster.set_health_points(hp_left)
                print(f"Has realizado {damage_points} de daño al monstruo! "
                      f"\n   {new_monster.name} => HP: {new_monster.health}")
                print()
                damage_points = damage_dealt(new_monster.attack_points, adventurer.defense_points)
                hp_left = adventurer.health - damage_points
                adventurer.set_health_points(hp_left)
                print(f"{new_monster.name} te ha atacado! Te ha quitado "
                      f"{damage_points} de Vida."
                      f"\n  {adventurer.name} => HP: {adventurer.health}")
                print()

            else:
                has_run = True

        if new_monster.health <= 0 and not has_run:
            print(f"Has logrado matar a {new_monster.name} de la raza {new_monster.race} eres un Heroe!")
            print()
            input("Presiona ENTER para continuar")
            print()
        if has_run:
            print(f"Has huido exitosamente, descansa para tu proxima aventura!")
            print()