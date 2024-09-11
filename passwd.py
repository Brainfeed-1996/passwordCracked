# import the libraries needed
import itertools
import string

# method takes as argument a string representing a password and returns the number of attempts
# and the password guessed. 
def bruteforce_attack(password):
    chars = string.printable.strip() # extract the characters without any trailing space
    attempts = 0     # variable to count attempts. 
    for length in range(1, len(password) + 1): # take the length of the input
        for guess in itertools.product(chars, repeat=length): # use the itertools to build a character sequence
            attempts += 1 # for every attempt increment the attempt counter 
            guess = ''.join(guess) # join the previously guess sequence with the new one
            if guess == password: # if the password is correct 
                return (attempts, guess) # return the password as well as number o guesses
    return (attempts, None) # otherwise return guesses 



# you can change the password here for different words 
# remember overly complicated passwords will require more computation time

###########################
password = "min" 
###########################


attempts, guess = bruteforce_attack(password)
if guess: # if the password is correctly guess output number of guesses and password 
    print(f"Password cracked in {attempts} attempts. The password is {guess}.")
else: # otherwise return failed and number of guesses 
    print(f"Password not cracked after {attempts} attempts.") 
    
# the platform will only allow the code to run for 5 seconds. 
# for longer passwords copy and paste the code into a python compiler and run it. 
