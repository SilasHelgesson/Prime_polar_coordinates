import math
import matplotlib.pyplot as plt

def get_input_number(message="Please enter integers only !"):
    try:
        return int(input("-> "))
    except KeyboardInterrupt:
        print("Goodbye !")
        exit()
    except:
        print(message)
        return get_input_number(message)

def welcome_screen(message="Funky things with prime numbers"):
    print("#"*(len(message)+2))
    print("#"+(message)+"#")
    print("#"*(len(message)+2))

def get_prime_number(last_num):
    for i in range(last_num + 1, last_num * 100):
        if i % 2 == 0:
            continue
        for j in range(3, math.isqrt(i) + 1):
            if i % j == 0:
                break
        else:
            return i

def get_primes(amount):
    if amount == 1:
        return [2]
    primes = [2]
    while len(primes) < amount:
        primes.append(get_prime_number(primes[-1]))
    return primes

def main():
    welcome_screen()
    print("Please enter your desires amount of simulation integers (I recommend 1000)")
    num = get_input_number()
    print("Plotting (Depending on the size of your input this may take a bit of time) ...")
    try:
        primes = get_primes(num)
        for i in primes:
            plt.polar(i, i, 'ro')
        plt.show()
    except KeyboardInterrupt:
        print("Goodbye !")
        exit()
    except:
        print("Unknown exception may be a result of plotting too many numbers")
        exit()

if(__name__ == "__main__"):
    main()
