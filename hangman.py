#built this independently with minial references for practice
#version updated with different categories :)

import random
import sys

fruit_word_list = ["APPLE","BANANA","CARROT","EGGPLANT","LETTUCE"]
pro_lang_word_list = ["PYTHON","JAVA","JAVASCRIPT","C","C++"]
car_word_list = ["VOLVO","HYUNDAI","TOYOTA","HONDA","SUZUKI"]
mil_word_list = ["RIFLE","MAGAZINE","BERET","BRASSARD","PISTOL"]
com_word_list = ["ASUS","ACER","DELL","TOSHIBA","LENOVO"]

rand_num = random.randint(0,2)
used_letters = []

#print(rand_num)

print('''
Hello! 
Welcome to to hangman made by JS!

Before we start, you will have to choose your category:
1. Fruits
2. Programming languages
3. Car brands
4. Items in the military
5. Laptop and computer brands

Key in the corresponding number for the category you want!
Alternatively, you may enter "Q" to quit.
''')

category = input().lower()
if category == "q":
    sys.exit()
elif category == "1":
    word_list = fruit_word_list
    print("Alright, you've chosen the 'Fruits' category")
elif category == "2":
    word_list = pro_lang_word_list
    print("Alright, you've chosen the 'Programming Languages' category")
elif category == "3":
    word_list = car_word_list
    print("Alright, you've chosen the 'Car brands' category")
elif category == "4":
    word_list = mil_word_list
    print("Alright, you've chosen the 'Military' category")
elif category == "5":
    word_list = com_word_list
    print("Alright, you've chosen the 'Laptop and computer brands' category")
    
print("You only have 10 tries, good luck!")

rand_word = word_list[rand_num]
#print(rand_word)#use this if you want to see the answer

def end_msg():
    play_again = input("Thank you for playing! Would you like to play again in the same category?\n").lower()
    if play_again in ["yes","yep","sure"]:
        #used_letters.clear()#somehow this doesnt work? ver prob?
        used_letters = []
        game_script()
    else:
        print("Alright, goodbye!")
        sys.exit()

def game_script():
    guess_taken = 0
    space = "-"*len(rand_word)
    while guess_taken <= 9:
        print(space)
        if space == rand_word:
            print("You win!")
            end_msg()
        user_guess = input("Take a guess!\n").upper()
        if user_guess == rand_word:
            print("You win!")
            end_msg()
        elif user_guess in used_letters:
            print("You've already tried this letter!")
            print(f"You have {10-guess_taken} tries left")
        elif user_guess in rand_word:
            print(f"Yes! {user_guess} is in the word!")
            used_letters.append(user_guess)
            new_space = ""
            for i in range (len(rand_word)):
                if user_guess == rand_word[i]:
                    new_space += user_guess
                else:
                    new_space += space[i]
            space = new_space
            guess_taken += 1
            print(f"You have {10-guess_taken} tries left")
        else:
            print(f"Sorry, {user_guess} is not in the word!")
            used_letters.append(user_guess)
            guess_taken += 1
            print(f"You have {10-guess_taken} tries left")
            
game_script()

print("You lose!")
end_msg()
