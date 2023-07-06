import random

class DiceSimulation:
    def __init__(self):
        self.response = "y"
    
    def play(self):
        while self.response == "y":
            no = random.randint(1, 6)
            
            if no == 1:
                print("---------")
                print("|       |")
                print("|   *   |")
                print("|       |")
                print("---------")
            elif no == 2:
                print("---------")
                print("| *     |")
                print("|       |")
                print("|     * |")
                print("---------")
            elif no == 3:
                print("---------")
                print("| *     |")
                print("|   *   |")
                print("|     * |")
                print("---------")
            elif no == 4:
                print("---------")
                print("| *   * |")
                print("|       |")
                print("| *   * |")
                print("---------")
            elif no == 5:
                print("---------")
                print("| *   * |")
                print("|   *   |")
                print("| *   * |")
                print("---------")
            elif no == 6:
                print("---------")
                print("| *   * |")
                print("| *   * |")
                print("| *   * |")
                print("---------")
            
            self.response = input("Pressione 'y' para jogar novamente ou 'n' para sair: ")
    
        print("Obrigado por jogar!")

# Código principal
if __name__ == "__main__":
    dice_game = DiceSimulation()
    dice_game.play()
