import random

lst=['s', 'w', 'g']
user_pt=0
comp_pt=0
i=0
chances=10

while i<chances:
           user_in=input("Enter Snake, Water or Gun: ")
           comp_in=random.choice(lst)

           if user_in==comp_in:
               print("Tie")

           elif comp_in=="w" and user_in=="s":
             user_pt=user_pt+1
           elif comp_in=="s" and user_in=="g":
             user_pt=user_pt+1
           elif comp_in=="g" and user_in=="w":
             user_pt=user_pt+1

           elif user_in=="w" and comp_in=="s":
              comp_pt=comp_pt+1
           elif user_in=="s" and comp_in=="g":
              comp_pt=comp_pt+1
           elif user_in=="g" and comp_in=="w":
              comp_pt=comp_pt+1

           else:
             print("try again")
            
           i=i+1
           print(f"Total no. cahnces left {chances-i} out of {chances} chances")

print("GAME OVER")

if user_pt==comp_pt:
    print("there is a tie")
    print(f"Your points-{user_pt} and computer's points-{comp_pt}")

elif comp_pt> user_pt:
     print("Computer Wins")
     print(f"Your points-{user_pt} and computer's points-{comp_pt}")

else:
     print("You Wins")
     print(f"Your points-{user_pt} and computer's points-{comp_pt}")





