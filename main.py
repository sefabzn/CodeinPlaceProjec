import random


# Generates random values for doors
def doorgenerate():
    Doors = {}
    FirstDoor = random.randint(0, 10) * 10  # values should be like 0,10,20,30,40.......
    SecondDoor = random.randint(0, 10) * 10
    ThirdDoor = random.randint(0, 10) * 10
    Doors['FirstDoor'] = FirstDoor
    Doors['SecondDoor'] = SecondDoor
    Doors['ThirdDoor'] = ThirdDoor
    return Doors


# asks user to select a door and shows its value
def askuser(Door):
    print("---------")
    SelectedDoor = input("Please select a  door : 1/2/3 \n")
    while SelectedDoor not in VALIDDOORS:
        SelectedDoor = input("Please select a VALID door !: ")
    print("---------")
    if SelectedDoor == "1":
        SelectedDoor = "FirstDoor"
    elif SelectedDoor == "2":  # Here, it turns the user input 1/2/3 to official door names
        SelectedDoor = "SecondDoor"
    elif SelectedDoor == "3":
        SelectedDoor = "ThirdDoor"
    print("You selected the " + str(SelectedDoor))
    DoorPoint = Door[SelectedDoor]
    print("The " + SelectedDoor + " has " + str(DoorPoint) + " points")
    return DoorPoint


# asks computer to select a door and shows its value
def askAI(Door):
    AIChoices = ['FirstDoor', 'SecondDoor', 'ThirdDoor']
    SelectedDoor = random.choice(AIChoices)  # chooses a door randomly
    print("AI selected the " + str(SelectedDoor))

    DoorPoint = Door[SelectedDoor]
    print(str(SelectedDoor) + " has " + str(DoorPoint) + " points")
    return DoorPoint


# declares the winner
def declarewinner(PointsUser, PointsAI):
    print("---------")
    if PointsUser > PointsAI:
        print("The user has won !")
    elif PointsUser < PointsAI:
        print("AI has won !")
    else:
        print("It is a draw !")


# checks if the user wants to use joker
def usejoker(Jokers, Doors):
    Answer = None
    if Jokers != 0:  # checks if the user has any jokers left
        Answer = input("Do you want to use joker ?  yes / no \n")
        while Answer not in VALIDANSWERS:
            Answer = input("Please type yes/no !:")

    if Answer == "yes":
        Doortobelooked = input("Which door do you want to look at ? 1/2/3 \n")
        while Doortobelooked not in VALIDDOORS:
            Doortobelooked = input("Please select a VALID door !:")

        Jokers -= 1
        if Doortobelooked == "1":
            Doortobelooked = "FirstDoor"
        elif Doortobelooked == "2":
            Doortobelooked = "SecondDoor"
        elif Doortobelooked == "3":
            Doortobelooked = "ThirdDoor"
        print(Doortobelooked + " has " + str(Doors[Doortobelooked]) + " points")
    return Jokers


# plays the game :D
def playgame(PointsUser, PointsAI, Jokers):
    TotalDoorValues = {"Door1": 0, "Door2": 0, "Door3": 0}
    print("Game starts now....")
    for i in range(1, 4):
        Doors = doorgenerate()
        TotalDoorValues = doorstatistics(Doors, TotalDoorValues)
        print("---------")
        print(str(i) + ". TURN\n---------")
        print("You have " + str(Jokers) + " jokers left.")
        Jokers = usejoker(Jokers, Doors)

        Points = askuser(Doors)

        PointsUser += Points
        print("---------")
        PointsAI += askAI(Doors)
        print("---------")
        print("You have " + str(PointsUser) + " Points.")
        print("AI has " + str(PointsAI) + " Points")

    declarewinner(PointsUser, PointsAI)
    seestatistics = input("Do you want to see the statistics yes/no \n")
    while seestatistics not in VALIDANSWERS:
        seestatistics = input("Please type yes/no !:")

    averagedoorvalues(TotalDoorValues, seestatistics)

    # collects all the values  door to door


def doorstatistics(Doors, TotalDoorValues):
    TotalDoorValues["Door1"] += Doors["FirstDoor"]
    TotalDoorValues["Door2"] += Doors["SecondDoor"]
    TotalDoorValues["Door3"] += Doors["ThirdDoor"]
    return TotalDoorValues


# calculates the average points of each door has
def averagedoorvalues(totaldoorvalues, seestatistics):
    if seestatistics == "yes":
        AverageDoor1 = round(totaldoorvalues["Door1"] / 3)  # to make them int values i used round  function
        AverageDoor2 = round(totaldoorvalues["Door2"] / 3)
        AverageDoor3 = round(totaldoorvalues["Door3"] / 3)
        print("Average point of Door 1 is", AverageDoor1)
        print("Average point of Door 2 is", AverageDoor2)
        print("Average point of Door 3 is", AverageDoor3)
        print("Good luck in another game")
    elif seestatistics == "no":
        print("Good luck in another game !")


VALIDANSWERS = ["yes", "no"]
VALIDDOORS = ["1", "2", "3"]
Jokers = 1
PointsUser = 0
PointsAI = 0


def main():
    playgame(PointsUser, PointsAI, Jokers)


if __name__ == '__main__':
    main()