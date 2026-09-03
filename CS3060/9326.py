def immutablilty_string():
    s1 = "Rossum"
    s1[2] = "a"
    s1 = "Guido von"
    # this will not work because strings are immutable

def f_string():
    price = 30
    discount = 20
    print("Original price was", price, "but after " ,discount, "% discount, it is now", price * (discount / 100))
    print(f"Original price was {price} but after {discount} % discount, it is now {price * (discount / 100)}")


def input_string():
    s0 = "Type your name: "
    s1 = input(s0)
    x = int(input("type a number: "))
    y = input(x*7)

def in_class_exercise():
    s1 = input("secret number is: ")
    guess = None
    while guess != s1:
        guess = input("guess the secret number: ")
        if guess > s1:
            print("too high")
        elif guess < s1:
            print("too low")
        else:
            print("you guessed it!")


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

    
    

    

def main():
    #f_string()
    #input_string()
    in_class_exercise()




main()