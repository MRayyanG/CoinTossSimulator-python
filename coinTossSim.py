import random

def main():

    while True:


        choice = input("Press 0 if you want to exit, or any key if you want to simulate coin toss: ").strip()

        if choice == '0':
            print("BYE!")
            break

        while True:

            times = input("Enter the number of times you want to simulate the toss: ").strip()

            if times.isnumeric() == False: # msg
                print("Enter a valid number: ")

            times = int(times) # convert to int

            if times != 0:
                break # exit loop

        # for a coin toss, we will generate two variables, 1 for H and 2 for T
        heads = 1
        tails = 0

        tosser(heads, tails, times) # this function will deal with tossing of coin

        # we will generate a string, that will store the results of the tosses, like a binary code
        # a count function will then check how many heads and tails are there

##################################

def counter(string): # this function will count and print the result

    headsNumber = string.count('1') # number of heads
    tailsNumber = string.count('0') # number of tails

    print("Heads: " + str(headsNumber))
    print("---------------------------")
    print("Tails: " + str(tailsNumber))

#############################
def tosser(heads, tails, times):

    storer = "S" # s for start, will help in file saving

    for i in range(times): # coin toss in range function
        
        result = str(random.randint(tails, heads)) # store in result

        # generate a string and store the tosses in it
        storer = storer + result

    #call counter function
    counter(storer)

############################

if __name__ == '__main__':
    main()

       

    

