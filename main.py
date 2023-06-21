import random

OUTCOME = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}

def rules(user, cpu):
    if user == 'Paper' and cpu == 'Rock':
        return True
    elif user == 'Rock' and cpu == 'Scissors':
        return True
    elif user == 'Scissors' and cpu == 'Paper':
        return True
    elif user == cpu:
        return "Remis"
    else:
        return False
    
def getUserTurn():
    userTurn = input("Wybierz kamień, papier lub nożyce:\n1.Kamień\n2.Papier\n3.Nożyce\n")
    for key, value in OUTCOME.items():
        if int(userTurn) == key:
            print(f"Twój wybor: {value}")
            return value

def getCpuTurn():
    cpuTurn = random.randint(1,3)
    for key, value in OUTCOME.items():
        if cpuTurn == key:
            print(f"Wybór komputera: {value}")
            return value
    
def main():
    userWins = 0
    cpuWins = 0
    while True:
        match rules(getUserTurn(), getCpuTurn()):
            case True:
                print("Wygrales!")
                userWins += 1
                print(f"Twoj wynik: {userWins}")
                print(f"Wynik CPU: {cpuWins}\n")
            case False:
                print("Przegrales :(")
                cpuWins += 1
                print(f"Twoj wynik: {userWins}")
                print(f"Wynik CPU: {cpuWins}\n")
            case "Remis":
                print("Remis!")
                userWins += 1
                cpuWins += 1
                print(f"Twoj wynik: {userWins}")
                print(f"Wynik CPU: {cpuWins}\n")
                
        
main()