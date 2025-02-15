print("***** TO REACH DESTINATION *****")

print("*"*40)
name=input("enter your name : ")
print(f"Hello {name} welcome to my game")
print("*"*40)

should_we_play=input("DO you want play?(yes/no) : ").lower()

if should_we_play=='yes':
    print("we are gonna play")
     
    direction=input("enter the direction (left/right): ").lower()

    if direction=='left':
        print("you went left game over,try again")

    elif direction=='right':
        print("you went to right direction")

        choice=input("enter the choice (walk/ride): ").lower()

        if choice=='walk':
            print(" If you walked then you went to slow.so,you cannot reached the destination.")
            
            print("="*60)
            print('you cannot reached destination.you loss the game')
            print("="*60)

        elif choice=='ride':
            
            print(" If you ride then you went to fastly.so,you can reached the destination.")   

            print("="*60)
            print("You reached successfully. you win the game")
            print("="*60)

        else:
            print("It is invalid choice")    
            
    else:
        print("It is invalid direction")


elif should_we_play=='no':
    print("we are not playing")

else:
    print("It is the invalid to play the game")
