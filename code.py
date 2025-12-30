#Random Number, has to be imported before the start of the code
import random
#Set Up
name = ""
question = ""
answer = ""
random_number = random.randint(1,11)
#Testing if Random number generrator works
#print (random.randint(1,9))

#Control Flow
if name == "":
  print ("Question is: " + question )
if question == "":
  print ("Whats the question?")
if random_number == 1:
  answer = "Yes - definetly."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply haxy, try again."
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
elif random_number  == 11:
  answer = "Unlucky"
else:
  answer= "Error"

print (name + " asks:" + question)
print ("Magic 8-Ball's answer: "  + answer)
