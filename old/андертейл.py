import time
import random


# Функция для медленного вывода текста
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


# Класс для создания врагов
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0


# Класс игрока
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0


# Функция для боя
def battle(player, enemy):
    print_slow(f"Вы встретили {enemy.name}!")
    while player.is_alive() and enemy.is_alive():
        print_slow(f"Ваше здоровье: {player.health}")
        print_slow(f"Здоровье {enemy.name}: {enemy.health}")
        print_slow("1. Атаковать")
        print_slow("2. Действовать")
        print_slow("3. Пощадить")

        choice = input("Что вы выберете? (1/2/3): ")

        if choice == "1":
            damage = random.randint(1, player.attack)
            enemy.health -= damage
            print_slow(f"Вы атаковали {enemy.name} и нанесли {damage} урона!")
        elif choice == "2":
            print_slow(f"Вы попытались поговорить с {enemy.name}...")
            print_slow(f"{enemy.name} выглядит задумчивым.")
        elif choice == "3":
            print_slow(f"Вы решили пощадить {enemy.name}.")
            print_slow(f"{enemy.name} уходит, улыбаясь.")
            break
        else:
            print_slow("Неверный выбор. Попробуйте снова.")
            continue

        if enemy.is_alive():
            enemy_damage = random.randint(1, enemy.attack)
            player.health -= enemy_damage
            print_slow(f"{enemy.name} атаковал вас и нанес {enemy_damage} урона!")

    if player.is_alive():
        print_slow(f"Вы победили {enemy.name}!")
    else:
        print_slow("Вы проиграли...")


# Основная функция игры
def main():
    print_slow("Добро пожаловать в мир Undertale!")
    print_slow("Введите имя вашего персонажа:")
    player_name = input("> ")
    player = Player(player_name, health=20, attack=5)

    print_slow(f"Привет, {player.name}! Вы просыпаетесь в темной пещере...")
    print_slow("Перед вами два пути: налево и направо.")

    choice = input("Куда вы пойдете? (налево/направо): ")

    if choice == "налево":
        print_slow("Вы нашли сундук с сокровищами!")
        print_slow("Ваша атака увеличена на 2!")
        player.attack += 2
    elif choice == "направо":
        print_slow("Вы встретили монстра!")
        enemy = Enemy("Гостер", health=15, attack=3)
        battle(player, enemy)
    else:
        print_slow("Вы заблудились...")

    if player.is_alive():
        print_slow("Вы продолжаете свое путешествие...")
    else:
        print_slow("Игра окончена.")


if __name__ == "__main__":
    main()