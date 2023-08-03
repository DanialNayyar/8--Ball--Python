import random

# Intro message and getting name and details
print("Hello and Welcome to the Magic 8-Ball.")
random_number = random.randint(1, 11)
answer = ""

print("Hello, and Welcome to Magic 8 Ball game written in Python.")

name = input("What is your name? ")
print("Nice to meet you", name + ". Let's get started.")

question = input("What is your question, " + name + "? ")

# Check if the question is empty and ask again until it's not empty
#strip removes white space
while question.strip() == "":
    print("Please type a question.")
    question = input("What is your question, " + name + "? ")

#print(question)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you"
elif random_number == 7:
    answer = "My sources say so."
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Probably not true - try again"
elif random_number == 11:
    answer = "Unlucky"
else:
    answer = "Error"

print("The Ball says:", answer)
