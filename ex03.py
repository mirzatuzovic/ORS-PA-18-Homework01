def main():
    print("This program illustrades a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)
main()

# Uocavamo da u ovom slucaju pocevsi od 6. koraka pa nadalje vrijednost od x ne varira.