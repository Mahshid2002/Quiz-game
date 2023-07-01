print("Welcome to my quiz!")
play = input("Do you wanna play? ")
if play.lower() != "yes":

    quit()
print("Great! Let's play! :)) ")
score = 0 # allow us to count how many correct answer do we have    /  score += 1       ==       score = score + 1

answer = input("How many bits makes one byte? ").lower()
if answer == "8 bits":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")   

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")   

answer = input("The first program that run on a computer when computer boots up is? ").lower()
if answer == "operating system":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")   

answer = input("What is the name of the software that allows us to browse through web pages called? ").lower()
if answer == "browser":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")   

answer = input("What is the address given to a computer connected to a network called? ").lower()
if answer == "ip address":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")   

print("you got "  + str(score)  + " Correct answers!")
print("you got "  + str((score) / 5 * 100 ) +  " percent ") 
