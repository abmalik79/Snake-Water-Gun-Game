 #Snake,Water,Gun game
"""
game rules:
 1-  Snake vs. Water: Snake drinks the water hence wins.
 2-  Water vs. Gun: The gun will drown in water, hence a point for water.
 3-  Gun vs. Snake: Gun will kill the snake and win.
"""

import random
def game(choice):
   computer=random.choice([-1,0,1])   #it will generate a random number between (0,-1,1) for the computer
   
   while  True:         #while loop will check either the user inputed number is within the given choices or not 
       you = int(input("-1 = snake\n0 = gun\n1 = water\nEnter your choice: "))
       if you not in choice:
         print("invalid choice!...please choose from the following choices: ")
         continue
      
       print(f"You chose: {choice[you]} \nComputer choose: {choice[computer]}")
       if computer==you:
         return "game draw!"
       else:
          if (computer==0 and you==-1) or (computer==1 and you==0) or (computer==-1 and you==1):
            return "you lose!" 
          else:
            return "you win!"     

def main() :
   choice={
      -1:"snake",
      0:"gun",
      1:"water"
   }  

   play=game(choice)  
   print(play)

if __name__ == "__main__":
  main()
#i have done it!
#i have done it!
#i have done it!
#i have done it!
