import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.


def get_range():
    while True:
        range_start = input("Enter the start of the range: ")
        if range_start.isdigit():
            range_start = int(range_start)
            break
        else:
            print("Please enter a valid number.")
    while True:
        range_end = input("Enter the end of the range: ")
        if range_end.isdigit():
            range_end = int(range_end)
            if range_end < range_start:
                print("Please enter a valid number.")
            else:
                break
        else:
            print("Please enter a valid number.")
    return range_start, range_end


def pick_number(start, end):
    return random.randint(start, end)


def guess_number():
    while True:
        guess = input("Guess a number: ")
        if guess.isdigit():
            guess = int(guess)
            break
        else:
            print("Please enter a valid number.")
    return guess


def main():
    attempts = 1
    start, end = get_range()
    hidden_number = pick_number(start, end)
    while True:
        guess = guess_number()
        if guess == hidden_number:
            break
        else:
            attempts += 1
    if attempts > 1:
        print(f"You guessed the number in {attempts} attempts")
    else:
        print(f"You guessed the number in {attempts} attempt")


main()
