for zahl in range(1,31):
    if zahl%3 == 0 and zahl%5 == 0:
        print("fizzbuzz")
    elif zahl%3 == 0:
        print("fizz")
    elif zahl%5 == 0:
        print("buzz")
    else:
        print (zahl)
