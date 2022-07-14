import numpy as np
import re

# Uncomment and implement two of the following.  Refer to the Problem solving brief for specifications.






import re

s = input("ENTER THE STRING  : ")
id = input("ENTER STUDENT ID : ")

list=re.split(" ", s)
list_length=len(list)

for i in range(list_length):
    list[i] = list[i].lower()
    if (list[i] == "the" or list[i] == "an" or list[i] == "a"):
        list_item_length = len(list[i])
        list[i] = "*" * list_item_length

listToStr = " ".join(map(str, list))
res = " ".join((listToStr,id))

print (res)






print("\nFERTILIZER CALCULATOR\n")

#input the coefficients of equation

while True:
    an= float(input("ENTER NITROGEN CONTENT IN TYPE A FERTILIZER(kg) : "))
    ap= float(input("\nENTER PHOSPHATE CONTENT IN TYPE A FERTILIZER : "))

    bn= float(input("\nENTER NITROGEN CONTENT IN TYPE B FERTILIZER(kg) : "))
    bp= float(input("\nENTER PHOSPHATE CONTENT IN TYPE B FERTILIZER : "))

    n= float(input("\nENTER THE AMOUNT OF NITROGEN REQUIRED BY THE CROP(kg) : "))
    p= float(input("\nENTER THE AMOUNT OF PHOSPHATE REQUIRED BY THE CROP(kg) : "))

    if not (an>0 and ap>0 and bn>0 and bp>0):
        print("INVALID INPUT")
    else:
        break

#Cramers rule

def fertiliser(an,ap,bn,bp,n,p):
    D=(an*bp)-(ap*bn)
    Da=(n*bp)-(p*bn)
    Db=(an*p)-(ap*n)
    a=Da/D
    b=Db/D
    if(a>0 and b>0):
        return [a,b]
    else:
        return []

#result

res=fertiliser(an,ap,bn,bp,n,p)
if res:
    print("\nTYPE A FERTILIZER : {} kg\nTYPE B FERTILIZER : {} kg".format(res[0],res[1]))
else:
    print ("NO SOLUTION FOUND")






# def makeBet(headsOdds, tailsOdds, previousOutcome, state):
#  # bet =
#  # state = 
#  return (bet, state)


# The following will be run if you execute the file like python3 problem_solving.py
# Your solutions should not depend on this code.
# The automated marker will ignore any changes to this code; feel free to modify it
# but keep the if and the indenting as is
if __name__ == '__main__':
   try:
      print(censor('The cat ate a mouse.')) # should give "### cat ate # mouse. <n1234567>"
   except NameError:
      print("Not attempting censoring problem")

   try:
      print(fertiliser(1, 0, 0, 1, 2, 2)) # should give (2.0, 2.0)
   except NameError:
      print("Not attempting fertiliser problem")

   import random
   try:
      random.seed(0)
      totalprofit = 0
      for round in range(10000):
         if random.randint(0,1) == 0:
            headsprob = 0.7
         else:
            headsprob = 0.4

         previousOutcome = None
         state = None
         profit = 0
         odds = dict()
         for _ in range(100):
            odds['heads'] = random.uniform(1, 3)
            odds['tails'] = random.uniform(1, 3)
            
            bet, state = makeBet(odds['heads'], odds['tails'], previousOutcome, state)
            
            previousOutcome = 'heads' if random.random() < headsprob else 'tails'
            if bet == previousOutcome:
               profit += odds[bet] - 1
            elif bet != 'no bet':
               profit -= 1          # stake lost

         print("Probability of heads was", headsprob, "Profit was", profit)
         totalprofit += profit
      print("Average profit per run:", totalprofit / 10000)

   except NameError as e:
      print("Not attempting probability problem")