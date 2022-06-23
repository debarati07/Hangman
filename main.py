import random

import word_list

import pyfiglet

import art
  
result = pyfiglet.figlet_format("FRUITMAN");

print(result)
print("\n\n");
chosen_word=random.choice(word_list.words)

display=[];
for letter in chosen_word:
    display.append("_");
print(display);

lives=0;
endofgame=False;
while not endofgame:
    guess=input("guess a letter:");
    for pos in range(len(chosen_word)):
        letter=chosen_word[pos];
        if(guess==letter):
            display[pos]=guess;
            print(display);
       
    if guess not in display:
        print(art.FRUITMAN[lives]);
        print(f"YOU LOSE {lives+1} life");
        lives=lives+1;
    if(lives==7):
        endofgame=True;
        print("YOU LOSE");
        print(f"THE CORRECT ANSWER IS {chosen_word}");
    elif "_" not in display:
        endofgame=True;
        print("You WIN"); 
