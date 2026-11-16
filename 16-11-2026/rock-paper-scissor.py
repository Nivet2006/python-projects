def guess_number():
    low = 1
    high = 100

    while low <= high:
        mid = (low + high) // 2
        print(f"\nIs your number {mid}?")

        response = input(f"Enter 'h' if above number is high, 'l' if too low, 'c' if correct: ").lower()

        if response == 'c':
            print(f"Great! Your number is {mid}")
            return
        elif response == 'h':
            high = mid - 1      
        elif response == 'l':
            low = mid + 1     
        else:
            print("Invalid input. Please enter h, l, or c.")
guess_number()