import random
print("*****************************Game time 😁😫*******************************")
print("***This is guessing a number from a given inervals***")
print(" ")

chance_left=1
balance=0
is_passed=False
print("1st round😎")
correct=random.randint(1,5)
guess=int(input(" guess my number through 1 upto 5🙄🙄: "))
chance_left+=1
if guess==correct:
  print("you got it🤩🤩, ")
  balance+=5
  print(f"you have ${balance}💰")
  is_passed=True
elif guess!=correct:
  while chance_left<=3:
   guess=int(input(" guess again🤯: "))
   chance_left+=1
   if guess==correct:
    print("you got it🤩🤩, ")
    balance+=5
    print(f"you have ${balance}💰")
    is_passed=True
    break
   elif guess!=correct:
    print("you have failed😓😓")
  
if is_passed==True:
 print(" ")
 print("*******************************************")
 print("2nd round😎")
 correct=random.randint(6,15)
 chance_left=1
 is_passed=False
 guess=int(input(" guess my number through 6 upto 15🙄🙄: "))
 chance_left+=1
 if guess==correct:
  print("you got it🤩🤩, ")
  balance+=10
  print(f"you have ${balance}💰")
  is_passed=True
 elif guess!=correct:

  while chance_left<=3:
   guess=int(input(" guess again🤯: "))
   chance_left+=1
   if guess==correct:
    print("you got it🤩🤩, ")
    balance+=10
    print(f"you have ${balance}💰")
    is_passed=True
    break
   elif guess!=correct:
    print("you have failed😓😓")

if is_passed==True:
 print(" ")
 print("********************************************")
 print("3rd round😎")
 correct=random.randint(16,30)
 chance_left=1
 guess=int(input(" guess my number through 16 upto 30🙄🙄: "))
 chance_left+=1
 if guess==correct:
   print("you got it🤩🤩, ")
   balance+=15
   print(f"you have ${balance}💰")
 elif guess!=correct:
   
   while chance_left<=3:
    guess=int(input(" guess again🤯: "))
    chance_left+=1
    if guess==correct:
     print("you got it🤩🤩, ")
     balance+=15
     print(f"you have ${balance}💰")
     break
    elif guess!=correct:
      print("you have failed😓😓")
    
