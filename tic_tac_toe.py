l1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display(l1):
    print(f' {l1[0]}|{l1[1]}|{l1[2]}')
    print("__|_|__")
    print(f' {l1[3]}|{l1[4]}|{l1[5]}')
    print("__|_|__")
    print(f' {l1[6]}|{l1[7]}|{l1[8]}')
    print("  | | ")


win_x = False
win_o = False

while win_x == False and win_o == False:
    display(l1)
    print("\n\nPlayer 1's turn")
    def input_x():
        k = int(input("Enter your choice[1-9]: "))
        choice_x = k-1
        if l1[choice_x] == ' ':
            l1[choice_x] = 'X'
        else:
            print("Already Occupied")
            input_x()
    try:
        input_x()
    except Exception as myerror:
        print("Error Occured: ",myerror)
        input_x()

    if (l1[0] == l1[1] and l1[1] == l1[2] and l1[0] == 'X') or (l1[3] == l1[4] and l1[4] == l1[5] and l1[3] == 'X') or (l1[6] == l1[7] and l1[7] == l1[8] and l1[6] == 'X'):
        win_x = True
        break
    elif (l1[0] == l1[3] and l1[3] == l1[6] and l1[0] == 'X') or (l1[1] == l1[4] and l1[4] == l1[7] and l1[1] == 'X') or (l1[2] == l1[5] and l1[5] == l1[8] and l1[2] == 'X'):
        win_x = True
        break
    elif (l1[0] == l1[4] and l1[4] == l1[8] and l1[0] == 'X') or (l1[2] == l1[4] and l1[4] == l1[6] and l1[2] == 'X'):
        win_x = True
        break
    else:
        pass
    

    display(l1)
    
    print("\nPlayer 2's turn")
    def input_o():
        j = int(input("Enter your choice[1-9]: "))
        choice_o = j-1
        if l1[choice_o] == ' ':
            l1[choice_o] = 'O'
        else:
            print("Already Occupied")
            input_o()
    try:
        input_o()
    except Exception as myerror:
        print("Error Occured: ",myerror)
        input_o()
    if (l1[0] == l1[1] and l1[1] == l1[2] and l1[0] == 'O') or (l1[3] == l1[4] and l1[4] == l1[5] and l1[3] == 'O') or (l1[6] == l1[7] and l1[7] == l1[8] and l1[6] == 'O'):
        win_o = True
    elif (l1[0] == l1[3] and l1[3] == l1[6] and l1[0] == 'O') or (l1[1] == l1[4] and l1[4] == l1[7] and l1[1] == 'O') or (l1[2] == l1[5] and l1[5] == l1[8] and l1[2] == 'O'):
        win_o = True
    elif (l1[0] == l1[4] and l1[4] == l1[8] and l1[0] == 'O') or (l1[2] == l1[4] and l1[4] == l1[6] and l1[2] == 'O'):
        win_o = True
    else:
        pass

print()
display(l1)
print()
if win_x == True:
    print("Player 1 Wins")
elif win_o == True:
    print("Player 2 Wins")
else:
    pass
