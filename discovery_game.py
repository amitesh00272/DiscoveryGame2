import time
import random


class Discovery_game:
    
    
    @staticmethod
    def first_level():
        User_choice = input('Press [I] for game information and [S] for start the game --> ')
        if User_choice == 'S' or User_choice == 's' or User_choice == 'I' or User_choice == 'i':
            print('\nGame information:-')
            
            print('>Hello Users! I am Amitesh Kumar and I especially made this game for jassos.')
            print('>In this game there are  three level.')
            print('>In every level you find different types of jassos events.')
            print('Enjoy the game!!')
            print('Starting.....')
            for i in range(1):
                time.sleep(1.5)
                

                print('Lets Play!!')
                break

            print('\t\t\t\t\t\t<<<<< First Level >>>>>\n')
            print('>>Mr Mishra wife have kidnap')
            first_level = input('You want to go in the Mr Mishra home to solve this problem?\n')
            if first_level == 'Yes' or first_level == 'yes':
                print('>>Hello Mr Mishra I am jassos can i help you!!')
                time.sleep(1.8)
                print('Hello sir,sure you help me in this problem!!\n')
                time.sleep(1)
                print('>>How your wife had kidnap?')
                time.sleep(0.8)
                print('When i return back to my home from office I saw my wife automatically go other side of wall.\n')
                time.sleep(1)
                print('>>Lets go there!!')
                time.sleep(0.8)
                print('Ok sir!!\n')
                time.sleep(1)
                print('>>There are three door,how these doors are come there?')
                time.sleep(0.8)
                print("Don't no Sir!!\n")
                inside_door = input('You want to go inside the door?\n')
                if inside_door == 'Yes' or inside_door == 'yes':
                    print('\n<<<<There are three doors, choose any one.>>>>\n')
                    print('In First Door >> There are three dnagerous lion who not eat any food from 2 years.')
                    print('In Second Door >> In this door so many poisionus snake are present.')
                    print('In Last Door >> There are many types of wild fruits are present.')
                    
                    User_choice = input('Enter your choice here >>> ')
                    if User_choice == 'First door' or User_choice == 'first door':
                        print('\nCongratulation!! You won this level')     
                        next_level = input('Press (N) for next level and (Q) for quit the game.\n')
                        if next_level == 'N' or next_level == 'n':
                            print('Starting....')
                            time.sleep(1.2)
                            
                        else:
                            quit()
                        
                        
                    elif User_choice == 'Second level' or User_choice == 'second level':
                        print('\nOoops!! You loss this level')
                        print('If you go inside the second door then snakes will kill you.')
                    
                    elif User_choice == 'Last door' or User_choice == 'last door':
                        print('\nOoops!! You loss this level')
                        print('If you go inside the last door and you eat wild fruits then it dangerous for your life..')
                    
                    else:
                        print('Your choice is wrong.')
                        exit()
                
                else:
                    print('You loose this game!!!')
                    exit()


            else:
                print('You loose this game!!!')
                exit()
            
        else:
            print('Your choice is wrong!!')   
            quit
            


    @staticmethod
    def second_level():
        LeftRight = random.randint(1,2)
        print(LeftRight)
        print('\n\t\t\t\t\t\t<<<<< Second Level >>>>>\n')
        print('Welcome in this level!!')
        print('Starting....\n')
        time.sleep(2.5)
        
        UserChoice = input('Choose Left or Right\n')
        
        ####### By using random number #######
        
        if LeftRight == 1 and UserChoice == 'right' or UserChoice == 'Right':
            
                print('Your Choice Is Correct!!\n')
                print('There are so many Rupees in one box and in another box there is Your Favourite thing')
                UserChoice = input('Then,what you choose Rupees or Favorite thing?\n')
                
                if UserChoice == 'Favourite thing' or UserChoice == 'favourite thing':
                    print('You are honest person,you not forget your favourite thing!!\n')
                    print('You feel thirsty!! There is so many Water in pond and Honey on tree.')
                    UserChoice = input('What you want to drink Water or Honey?\n')
                    
                    if UserChoice == 'Water' or UserChoice == 'Water':
                        print('Only,Water is necessary to drench you thirsty neck.\nYour choice is correct!!\n')
                        print('\nCongratulation!! You won this level')     
                        next_level = input('Press (N) for next level and (Q) for quit the game.\n')
                        if next_level == 'N' or next_level == 'n':
                            print('Starting....')
                            time.sleep(1.2)
                            
                        else:
                            quit()
                            
                        
                    elif UserChoice == 'Honey' or UserChoice == 'honey':
                        print('There are big Bear on the tree,He will kill you.\nYou loose this game!!')
                        quit()
                        
                    else:
                        print('Error: This option is not present there')
                        quit()
                    
                
                elif UserChoice == 'Rupees' or UserChoice == 'rupees':
                    print('You greedy person!!\nYou are disqualify from this game.')
                    quit()
                    
                    
                else:
                    print('Error: This option is not present there')
                    quit()
            
        
        elif LeftRight == 2 and UserChoice == 'left' or UserChoice == 'Left':
            
                print('Your Choice Is Correct!!\n')
                print('There are so many Rupees in one box and in another box there is Your Favourite thing')
                UserChoice = input('Then,what you choose Rupees or Favorite thing?\n')
                
                if UserChoice == 'Favourite thing' or UserChoice == 'favourite thing':
                    print('You are honest person,you not forget your favourite thing!!\n')
                    print('You feel thirsty!! There is so many Water in pond and Honey on tree.')
                    UserChoice = input('What you want to drink Water or Honey?\n')
                    
                    if UserChoice == 'Water' or UserChoice == 'Water':
                        print('Only,Water is necessary to drench you thirsty neck.\nYour choice is correct!!\n')
                        print('\nCongratulation!! You won this level')     
                        next_level = input('Press (N) for next level and (Q) for quit the game.\n')
                        if next_level == 'N' or next_level == 'n':
                            print('Starting....')
                            time.sleep(1.2)
                            
                        else:
                            quit()
                        
                        
                    elif UserChoice == 'Honey' or UserChoice == 'honey':
                        print('There are big Bear on the tree,He will kill you.\nYou loose this game!!')
                        exit
                        
                    else:
                        print('Error: This option is not present there')
                        quit()
                   
                
                elif UserChoice == 'Rupees' or UserChoice.lower:
                    print('You greedy person!!\nYou are disqualify from this game.')
                    quit()

                else:
                    print('Error: This option is not present there')
                    quit()
        
        else:
            print('\nOoops your choice is wrong\nNow you are terminated from this game.')                   
            quit()
                 
    @staticmethod
    def final_level(score):
        print('\n\t\t\t\t\t\t<<<<< Second Level >>>>>\n')
        print('This is your final level.In this level there are only some difficulties.\n')
        print('Enjoy the last level!!!')
        
        print('Starting....\n')
        time.sleep(3)
        
        UserChoice = input('Which character you like so much Doremon or Sinchan?\n')
        if UserChoice == 'Doremon' or UserChoice == 'doremon':
            print('Now your name is Doremon for this level!!\n')
            print('Rooms: 1.Store Room or 2.Study Room')
            room1 = 'Store Room'
            room2 = 'Study Room'
            UserChoice = input('There is so many mouse in this room so In which room do you want to go?\n')
            if UserChoice ==  room1  or UserChoice == 'store room':
                print('Already,there are so many mouse in store room.')
                print('You know that doremon afraid from mouse.')
                exit()
            
            elif UserChoice == room2 or UserChoice == 'study room':
                print('\nUhh! This is safest place for me.')
                print('Now I am safe!!')
                print('Now I am going to end this game,I hope that you enjoy tis game!!!')
                score+=5
                
            
            else:
                print('Incorrect choice!!!')
                exit()
            
            
        
        elif UserChoice == 'Sinchan' or UserChoice == 'sinchan':
            print('Now your name is Sinchan for this level!!')
            exit()
            
        else:
            print('Your choice is wrong!!')
            quit()
        
        


if __name__ == '__main__':
    Amitesh_Kumar = Discovery_game()
    Amitesh_Kumar.first_level()
    Amitesh_Kumar.second_level()
    Amitesh_Kumar.final_level(5)
    #input()