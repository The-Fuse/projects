import random
print("Best of times played is the criteria for winning")
print("Input your choice as index of the following:")
print("1.scissor")
print("2.Rock")
print("3.Paper")
n=int(input("How many times you want to play:"))
i=0
resources=["Scissor","Rock","Paper"]
winning_count=0
while i<n:
    i+=1
    computer=random.randint(0,2)
    user=int(input("Enter your choice:"))
    if user>0 and user<4:
        if user == 1 and computer == 2:
            winning_count += 1
            print("Computer chice:", resources[computer])
            print("Yup!!, you wins.")
        elif user == 2 and computer == 0:
            winning_count += 1
            print("Computer chice:", resources[computer])
            print("Yup!!, you wins.")
        elif user == 3 and computer == 1:
            winning_count += 1
            print("Computer chice:", resources[computer])
            print("Yup!!, you wins.")
        elif user == computer + 1:
            print("Computer choice:", resources[computer])
            print("It's clash!!")
        else:
            print("Computer chice:", resources[computer])
            print("Try again")
    else:
        print("Wrong input by user!")
if winning_count>n-winning_count:
    print("You wins the match!!")
elif winning_count==n-winning_count:
    print("It's tie")
else:
    print("Sorry!!, you losed it!")



