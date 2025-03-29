import random

class Player: #Used for both Hero and Villain
    def __init__(self, name):
        self.name = name
        self.life_points = 100
        self.strength = 0  #Strength will be determined before each fight

    def set_strength(self):
        self.strength = random.randint(1, 50)

    def receive_damage(self, damage): #How Damage is calculated
        self.life_points -= damage
        if self.life_points < 0:
            self.life_points = 0

    def is_alive(self):
        return self.life_points > 0

def battle(player1, player2): #Battle Function
    player1.set_strength()
    player2.set_strength()

    print(f"\n{player1.name} strength: {player1.strength}")
    print(f"{player2.name} strength: {player2.strength}")

    if player1.strength > player2.strength:
        damage = player1.strength - player2.strength
        player2.receive_damage(damage)
        print(f"{player1.name} wins! {player2.name} loses {damage} life points.")
    elif player2.strength > player1.strength:
        damage = player2.strength - player1.strength
        player1.receive_damage(damage)
        print(f"{player2.name} wins! {player1.name} loses {damage} life points.")
    else:
        print("It's a tie! No one loses life points.")

def main():
    hero = Player("Captain America")
    villain = Player("Red Skull")

    round_number = 1
    while hero.is_alive() and villain.is_alive():
        print(f"\n--- Round {round_number} ---")
        choice = input("Do you want to (H)it or (Q)uit? ").strip().lower()

        if choice == 'q':
            print("\nYou chose to quit the battle. Game over!")
            break
        elif choice == 'h':
            battle(hero, villain)
            print(f"{hero.name}: {hero.life_points} life points")
            print(f"{villain.name}: {villain.life_points} life points")
            round_number += 1
        else:
            print("Invalid input. Please enter 'H' to hit or 'Q' to quit.")

    if hero.is_alive() and villain.is_alive():
        print("\nThe battle was ended by the player.")
    elif hero.is_alive():
        print(f"\n{hero.name} wins the battle!")
    else:
        print(f"\n{villain.name} wins the battle!")

if __name__ == "__main__":
    main()
