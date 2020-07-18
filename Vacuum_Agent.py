"""
Name : Aditi Pandey
Roll no: 081
PRN : 0120180293
"""

import random

''' Octal Representation '''
# 0 => both rooms are clean
# 1 => room B is dirty A is clean
# 2 => room A is dirty B is clean
# 3 => both rooms are dirty

def agent(dirt, currPosAg):
  print("Starting the cleaning process . . . ")
  print("Agent position . . . is at room", currPosAg)
  print("Dirt detected in room -> "),
  if (dirt == 1):
    print("B")
    if(currPosAg == 'A'):
      print("Moving from room",currPosAg," ---> B")
      currPosAg = 'B'
      print("Cleaning room B")
    else:
      print("Cleaning room B")
  elif (dirt == 2):
    print("A")
    if(currPosAg == 'A'):
      print("Cleaning room A")
    else:
      print("Moving from room",currPosAg," ---> A")
      currPosAg = 'A'
      print("Cleaning room A")
  elif (dirt == 3):
    print("A and B")
    print("Cleaning room ",currPosAg)
    print("Moving from room",currPosAg," ---> "),
    if(currPosAg == 'A'):
      print("B")
      currPosAg = 'B'
      print("Cleaning room B")
    else:
      print("A")
      currPosAg = 'A'
      print("Cleaning room A")
  else:
    print("Both rooms are CLEAN")
  return(currPosAg)

def dirtGen():
  dirt =(random.randint(0, 3))
  return(dirt);

def choicePre():
  inpt = input("Select an operation : ")
  return (inpt)

def main():
    print("DIRT STATUS NUMBERS")
    print("         0 => both rooms are clean")
    print("         1 => room B is dirty A is clean")
    print("         2 => room A is dirty B is clean")
    print("         3 => both rooms are dirty\n\n")
    dirt = 0;
    select = 1;
    score = 0;
    currPosAg = 'A'
    print ("OPERATION LIST")
    print ("         1 - > Run the agent")
    print ("         2 - > Generate Dirt")
    print ("         3 - > Display Score")
    print ("         4 - > Exit")
    while(select):
      inpt = choicePre()
      print("Input = ",inpt)
      if inpt == '1':
        score += dirt
        currPosAg = agent(dirt, currPosAg)
        dirt = 0
        print("\n\n")
      elif inpt == '2':
        dirt = dirtGen()
        print("Current dirt status = ",dirt)
        print("\n\n")
      elif inpt == '3':
        print("Current Score = ",score)
        print("\n\n")
      elif inpt == '4':
        print("Exiting . . . ")
        select = 0
      else:
        print("Wrong option chosen, try again !\n\n")


if __name__ == "__main__":
    main()







#OUTPUT :

"""
DIRT STATUS NUMBERS
         0 => both rooms are clean
         1 => room B is dirty A is clean
         2 => room A is dirty B is clean
         3 => both rooms are dirty


OPERATION LIST
         1 - > Run the agent
         2 - > Generate Dirt
         3 - > Display Score
         4 - > Exit
Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room A
Dirt detected in room -> 
Both rooms are CLEAN



Select an operation : 2
Input =  2
Current dirt status =  3



Select an operation : 3
Input =  3
Current Score =  0



Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room A
Dirt detected in room -> 
A and B
Cleaning room  A
Moving from room A  ---> 
B
Cleaning room B



Select an operation : 3
Input =  3
Current Score =  3



Select an operation : 2
Input =  2
Current dirt status =  1



Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room B
Dirt detected in room -> 
B
Cleaning room B



Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room B
Dirt detected in room -> 
Both rooms are CLEAN



Select an operation : 2
Input =  2
Current dirt status =  3



Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room B
Dirt detected in room -> 
A and B
Cleaning room  B
Moving from room B  ---> 
A
Cleaning room A



Select an operation : 3
Input =  3
Current Score =  7



Select an operation : 2
Input =  2
Current dirt status =  3



Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room A
Dirt detected in room -> 
A and B
Cleaning room  A
Moving from room A  ---> 
B
Cleaning room B



Select an operation : 2
Input =  2
Current dirt status =  0



Select an operation : 1
Input =  1
Starting the cleaning process . . . 
Agent position . . . is at room B
Dirt detected in room -> 
Both rooms are CLEAN



Select an operation : 4
Input =  4
Exiting . . . 
"""
