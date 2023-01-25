print("Welcome to my geography quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

num_of_questions = int(input("How many questions would you like to answer? "))

for i in range(num_of_questions):
    answer = input("What is the capital of France? ")
    if answer.lower() == "paris":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the highest mountain in the world? ")
    if answer.lower() == "mount everest":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the longest river in Africa? ")
    if answer.lower() == "the nile":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the largest ocean in the world? ")
    if answer.lower() == "pacific ocean":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / num_of_questions) * 100) + "%.")