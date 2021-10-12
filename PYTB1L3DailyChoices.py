print("Your alarm rings, do you GETUP or go back to sleep ?")
choice = input()
if choice == 'GETUP':
    print("You get out of bed and feel fresh!")
    print("Your family is having breakfast, will you join them or eat alone ?")
    choice = input()
    if choice == 'join them':
        print("You get out of bed and feel fresh!")
    elif choice == 'eat alone':
        print("you had to make your own breakfast")
    else:
        print(choice, " you didn't eat breakfast")

    print("You're now fully awake, what will you do today, game with vriends?, go to the gym? or stay at home?")
    choice = input()
    if choice == 'game with vriends':
        print("You and your vriends had a fun time!")
    elif choice == 'go to the gym':
        print("you had a hard workout")
    else:
        print(choice, " you watched some episodes of your favorite TV show")

elif choice == 'go back to sleep':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")


