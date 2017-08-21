def FizzBuzz(start=1, stop=101):
    num = 0
    for num in range(start,stop):
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print (num)

FizzBuzz()
