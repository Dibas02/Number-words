num = int(input("Enter a number: "))

def numberword(num):
    if num == 20:
        print("twist")
    elif num == 15:
        pass
    elif num == 5:
        print("fizz")
    elif num == 3:
        print("buzz")
    else:
        print(num)

numberword(num)