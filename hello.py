from random import randint

name = input("What is your name? ")

print("Hello "+name+"!")

quest = input("What is your quest? ")

rand_int = randint(1,3) #(Inclusive)

if rand_int == 1:
    color = input("What is your favorite color? ")
    third_question = "color"
elif rand_int == 2:
    cap_of_assyria = input("What is the capitol of Assyria? ")
    third_question = "assyria"
elif rand_int == 3:
    swallow = input("What is the airspeed velocity of an unladen swallow? ")
    third_question = "swallow"

