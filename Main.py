import random
import math
lower=int(input("Enter lower nunber: "))
upper=int(input("Enter higher number: "))
x=random.randint(lower,upper)
print("\n\t You have only", round(math.log(upper-lower+1,2)),"chances to gues>
count=0
while count<math.log(upper-lower+1,2):
 count += 1
 guess = int(input("Guess a nunber: "))
 if x==guess:
  print("Congratulations you did it in",count,"try")
  break
 elif x>guess:
  print("You guessed too low")
 elif x<guess:
  print("You guessed too high")
if count >= math.log(upper-lower+1,2):
 print("The number is ",x)
 print("Better luck next time!")
