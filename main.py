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

def checkWin():
    if rules(getUserTurn(),getCpuTurn()):
        print("Wygrywasz!\n")
    else:
        print("Niestety przegrywasz :(\n")
        
def main():
    while True:
        checkWin()

main()