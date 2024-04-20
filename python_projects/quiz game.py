print("welcome to quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay ! lets play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random acess memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "Power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

