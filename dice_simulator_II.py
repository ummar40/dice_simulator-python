import random                #in built python function used to import random numbers(int,float etc)

user_input = 'y'             #y is user input and in order to keep simulating we'll keep pressing y(yes)
while user_input=='y':
    x = random.randint(1,6)  #import random integers from 1-6
    if x==1:
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
        
    if x==2:
        print("┌─────────┐")
        print("│ ●       │")
        print("│         │")
        print("│       ● │")
        print("└─────────┘")
        
    if x==3:
        print("┌─────────┐")
        print("│ ●       │")
        print("│    ●    │")
        print("│       ● │")
        print("└─────────┘")
    if x==4:
        print("┌─────────┐")
        print("│  ●    ● │")
        print("│         │")
        print("│  ●    ● │")
        print("└─────────┘")
        
    if x==5:
        print("┌─────────┐")
        print("│  ●    ● │")
        print("│    ●    │")
        print("│  ●    ● │")
        print("└─────────┘")
        
    if x==6:
        print("┌─────────┐")
        print("│  ●    ● │")
        print("│  ●    ● │")
        print("│  ●    ● │")
        print("└─────────┘")
        
    user_input = input("Do You want to continue? y for YES or press any key to exit")