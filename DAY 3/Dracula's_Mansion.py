import time

ascii_art = (r'''
                                 A
                                / \
                               /   \
              A               <_____>
             / \            _ _|_Y_|_ _
            /   \           ]=I=I=I=I=[
           <_____>           \-|-|-|-/ 
         _ _|_Y_|_ _          |     |
         ]=I=I=I=I=[         _|_ _  |            A
          \-|-|-|-/          ]=I=[  |      A    / \
           |     |    A       \|/   |     / \  /   \
           |     |   / \      |Y    |    /   \<_____>
           | /^\ |  /   \     |     |   <_____>|   |
           | | | | <_____>    | []  | _ _|_Y_|_|   |
           | |_| |  |   |     |     | ]=I=I=I=I|   |
           |     | _|_Y_|_ _  |     |  \-|-|_ _|_Y_|_ _
           |     |=I=I=I=I=[  |  [] |       ]=I=I=I=I=[
        _ _|_ _ _|_-_-|-|-/_ _|_ _ _|_ /^\   \-|-|-|-/ 
        ]=I=I=I=I=I=[    | ]=I=I=I=I=I=|O|    |     |
         \-|-|-|-|-/     |  \-\-|-|-/-/ \|    | /^\ |
          |    [] | _ _ _|_ _|  _____|_ |     | | | |
          | []    |=I=I=I=I=[| /vvvvvvv\|     | === |
       _ _|_ _ _ _|_-_-|-|-/ |/vvvvvvvvv\     |     |
       ]=I=I=I=I=I=I=[    |  <===========> _ _|_ _ _|_ _
        \-\--|-|--/-/     |  || []   [] |  ]=I=I=I=I=I=[
         |         | _ _ _|_ ||_ _ _ _ _|_ _\--|-|-|--/
         |         |=I=I=I=I=I=I=I=I=I=I=I=I=|       |
         | []      |-=-=-=-=-=-=-=-=-=-=-=-=-|     []|
         |         |           ___           |       |
         |         |          /   \          |       |
         |         |         |     |         |       |
       _/|         |\_       |     |       _/|       |\_ ''')

# Intro
print(f"\033[31m {ascii_art} \033[0m")
time.sleep(1)

print("You suddenly felt a jolt...")
time.sleep(1.75)

print("You wake up and look around...")
time.sleep(1.75)

print("It's not your house anymore...")
time.sleep(1.75)

print("\t\033[3mWhere am I\033[0m")
time.sleep(1.75)

print("You feel a strange presence...")
time.sleep(1.75)

print("You turn around and you can't believe what you are looking at...")
time.sleep(1.75)

print("\033[3m\tIT'S DRACULA!!!!\033[0m")
time.sleep(1.75)

print("You try to run but it's all in vain")
time.sleep(1.75)

print("Dracula speaks to you...")
time.sleep(1.75)

print("\t\033[1;3;31mYOU ARE IN MY CASTLE CHILD, I CAN'T LET YOU LEAVE NOW\033[0m")
time.sleep(1.75)

print("Looking at your scared but confused face, DRACULA shows mercy and gives you one last chance to get away...")
time.sleep(2)

print("\033[1;3;31mRUN BOY... BUT REMEMBER - ONE WRONG MOVE AND YOUR SOUL'S MINE\033[0m")
time.sleep(1.75)

# First choice - left/right
path1 = input("\nYou leave the room and see the path fork into two. Where are you going \033[1mLEFT\033[0m or \033[1mRIGHT\033[0m?\n").lower().strip()
if path1 in ('r', 'right'):
    print("Wrong Turn, You don't have anything left.")  # intentional
else:
    print("Seems like you chose the right path.")  # intentional
    time.sleep(1)

    # Second Choice - doors
    door = input("You run a little further and you see 3 doors.\n\033[1;34mBlue Door\033[0m as cold as ice...\n\033[1;31mRed Door\033[0m that reeks of blood...\n\033[1;32mGreen Door\033[0m stinks of animals and insects\n").lower().strip()
    if door in ('blue', 'b'):
        print("What were you thinking going in there? Now you are just moments away from freezing....")
    elif door in ('green', 'g'):
        print("What were you thinking going there? Those hungry animals now wait for you to take a step ahead....")
    elif door in ('red', 'r'):
        print("Not everything that seems dangerous is bad. Don't smile—you were just lucky...")
        
        # Third choice - wait/swim
        river = input("As you walk through that door, everything around you changes. You find yourself on a muddy river bank. You think you are OUT but you feel shivers down your spine. What are you gonna do — \033[1mWait here\033[0m or \033[1mSwim across\033[0m?\n").lower().strip()
        if river in ('wait', 'w'):
            print("Should have trusted your gut. Now the mud is swallowing everything—EVEN YOU.....")
        elif river in ('swim', 's'):
            print("Soaked and shivering, you drag yourself out of the muddy riverbank.")
            time.sleep(1)
            print("A long, unending road stretches before you, its surface slick with rain.")
            time.sleep(1)
            print("As you move along, the path branches — to your \033[1mleft\033[0m, a trail disappears into a dense, shadowy forest.")
            time.sleep(1)
            print("To your \033[1mright\033[0m, the ground slopes toward a broken bridge, creaking in the wind.")
            time.sleep(1)
            last_chance = input("\nWhich way will you go? ").lower().strip()

            if last_chance in ('left', 'l'):
                print("You turn left, swallowed by the forest's darkness.\nA shadow descends, fangs pierce deep.\nYour journey ends here....")
            elif last_chance in ('right', 'r'):
                print("You take the right path, chasing the glow of lanterns.\nThe night air grows clear, the castle fading behind.\nYou are free.")
            elif last_chance in ('straight', 'forward', 'ahead', 's'):
                print("Jason! JASON!! JASSSOOONNN!!! WAKE UP")
                print("You wake up sweating, realizing all was just a nightmare.")
                print("You go to your mom, she looks at you and says: why do you look like you have been playing in\033[31m mud\033[0m?")
