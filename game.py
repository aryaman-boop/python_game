import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(10./90)
health= 10

inp_name= input("What's your name?")
inp_age= input("What's your age?")
if int(inp_age) >= 12:
    inp_play = input("Do you want to play?[y/n]")
    if inp_play == "y":
        print("You are old enough to play")
        if inp_name == "Special":
            sprint("Welcome Special One!")
            sprint("Worlds blessing!")
            sprint("Your health will increase by 10.")
            health = health+10
            print ("Your health is now",health)
        else:
            print("Welcome",inp_name)
            sprint("Your health is 10")
        first_choice=input("You start your adventure and a fork in the road comes, where do you go?[left/right]")
        if first_choice =="left":
            sprint("You went left. You see a lost person.")
            inp_help= input("Do you help them?[y/n]")
            if inp_help== "y":
                sprint("You meet another adventurer. You gain an companion.")
                sprint("You see a monster.")
                inp_fightf= input("Do you fight it?[y/n]")
                if inp_fightf=="y":
                    sprint("You and your companion deafeat it with the power of friendship.")
                    sprint("You go on adventures all your life.")
                elif inp_fightf == "n":
                    sprint("You try to escape but the monster attacks you. You and your companion barely escape. After this you choose to do farming.")
            elif inp_help=="n":
                sprint("You see a monster.")
                inp_fight= input("Do you fight it?[y/n]")
                if inp_fight=="y":
                    sprint("You fight the monster but you barely escape with your life.")
                    health = health-8
                    print("Your health is now",health)
                elif inp_fight=="n":
                    sprint("Smart choice you escaped with your life.")
        if first_choice=="right":
            print("You went down the road. You see the carraige being attacked by bandits.")
            yes_no = input("Do you save the carriage?[y/n]")
            if yes_no== "y":
                sprint("you fight them of but you get some damage as well. you lose 2 health")
                health= health-2
                print("your health is now",health)
                sprint("You save the royal heir and they fall in love with you. You marry them and happily live your life.")
            elif yes_no=="n":
                sprint("You meet a merchant and you become the heir to his company and live a lavish life.")

    else:
        sprint("why did you come here in the first place.")
else :
    print("You aren't old enough to play, come back in a few years young adventurer.")
