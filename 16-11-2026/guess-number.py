def guess_number():
    low = 1
    high = 100
    while low <= high:
        mid = (low + high) // 2
        print(f"Is your number {mid}?")
        response = input("Enter 'h' if too high, 'l' if too low, 'c' if correct: ")
        if response == 'c':
            print(f"Great! Your number is {mid}")
            return
        elif response == 'h':
            high = mid - 1
        else:
            low = mid + 1
    print("I couldn't guess your number.")
guess_number()