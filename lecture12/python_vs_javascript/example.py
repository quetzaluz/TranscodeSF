import random

def try_guess(num, guess):
    if guess < num:
        print guess, "is too low!"
    elif guess > num:
        print guess, 'is too high!'
    else:
        print guess, "is right. You win!"

# Guess randomly until you win
secret_number = random.randint(1, 5)
guess = None
while guess != secret_number:
    guess = random.randint(1, 5)
    try_guess(secret_number, guess)


def is_prime(x):
    for num in range(2, x):
        # If x divides num evenly, then x is a factor of num.
        if x % num == 0:
            return False
    return True

for y in [2, 6, 13, 8, 20]:
    print "%d is prime?" % y, is_prime(y)


some_list = [1, 2, 4]
some_dict = {}
some_dict['key_string'] = True
some_dict[3] = some_list
some_dict[3][1] = 2
print some_dict[3][1], "should be", 2
