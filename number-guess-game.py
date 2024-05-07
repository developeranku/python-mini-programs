"""
- Its a Number guessing game, in which the user selects a range.
- Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
- Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
 """

import random
import math
import sys


print("---------- Please pick a range between two numbers and then pick a guess ----------")


start = int(input("Please enter start range for number: "))
end = int(input("Please enter ending range for number: "))


if start > end:
    raise TypeError("End number should be less than start")

available_choices = round(math.log(end - start, 2))
attempted_choices = 0
computer_picked_num = random.randint(start, end)

print(f"You have {str(available_choices)} chances to guess the number")

while (available_choices > attempted_choices):
    attempted_choices += 1
    user_pick = int(input("Please enter guessed number: "))
    if user_pick > computer_picked_num:
        print("You guessed higher number")
    elif user_pick < computer_picked_num:
        print("You guessed lower number")
    elif user_pick == computer_picked_num:
        total_tries = (available_choices)
        print(f"Yayy, You guessed it right in {attempted_choices} tries")
        sys.exit()

if available_choices <= attempted_choices:
    print(f"The number is: {computer_picked_num}")
    print("Better luck next time")
    sys.exit()
