def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * (x - x * x)
        y = 3.9 * (y - y * y)
        print(round(x, 3), round(y, 3))


main()