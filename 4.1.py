import random

computer_number = random.randint(1, 10)
while True:
    number = int(input("Enter Number : "))
    if number == computer_number: #3 == 6
        print("Correct")
        break
    elif number < computer_number: #3 < 6
        print("Number is lower")
    else:
        print("Number is bigger")