field=['1','2','3',
       '4','5','6',
       '7','8','9']

current_player=1

def draw(field):
    print(f"{field[0]} {field[1]} {field[2]}")
    print(f"{field[3]} {field[4]} {field[5]}")
    print(f"{field[6]} {field[7]} {field[8]}")
    # print("\n")

def endgame(field,player):
    draw (field)
    print(player + "wins")
    exit()



def check(field):
    players=[ 'X','O' ]

    for player in players:
        if field[0]==player and field[1]==player and field==[2]==player:
            endgame(field,player)

        elif field[3]==player and field[4]==player and field==[5]==player:
            endgame(field,player)

        elif field[6]==player and field[7]==player and field==[8]==player:
            endgame(field,player)

        elif field[0]==player and field[3]==player and field==[6]==player:
            endgame(field,player)

        elif field[1]==player and field[4]==player and field==[7]==player:
            endgame(field,player)

        elif field[2]==player and field[5]==player and field==[8]==player:
            endgame(field,player)

        elif field[0]==player and field[4]==player and field==[8]==player:
            endgame(field,player)

        elif field[2]==player and field[4]==player and field==[6]==player:
            endgame(field,player)


draw(field)

while True:
    print("\n")
    x=int(input(f"player {current_player} where?: "))
    print(x)
    
    if current_player==1:
        field[ (x-1) ]='X'
        current_player=0
    else:
        field[ (x-1) ]='O'
        current_player=1  

    check(field)
    draw(field)
    