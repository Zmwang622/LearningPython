
import random
def main():
   num = int(input("Guess a number from 1 to what number? ")) 
   correct_number = random.randint(1,num)
   try_count = 0
   found = False
   while not found:
       user_guess = int(input("Pick an number between 1 and " + str(num)+": "))
       try_count += 1
       if(user_guess<correct_number):
           print("Your number was too low. Try again!")
       elif(user_guess == correct_number):
           found = True
       else:
           print("Number was too high. Try again!")

   print("Congrats you beat the game! The number was ", correct_number, " and it took you ", try_count, " tries!")
   
main()