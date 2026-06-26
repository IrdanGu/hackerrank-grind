def bouncer(numbers):
    print("Club doors are opening...")
    for i in numbers:
        if i % 2 == 0:
            print(f"Number {i} gets to enter!")
        else:
            print(f"Number {i} is turned away at the door.")

# Test the logic with a list of guests
guest_list = [1, 2, 3, 4, 5, 8, 11]
bouncer(guest_list)
