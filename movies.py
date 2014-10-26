def movies():
    age=input("Enter age (child, middle school, high school, or other): ")
    weather=input("Enter weather(rainy, sunny, hailing, snowing, or other): ")
    if age=="child":
        if weather=="sunny":
            print("Pay $2.")
        elif weather=="snowing":
            print("Pay $1.50.")
        else:
            print("You're in for free!")
    elif age=="middle school":
        if weather=="rainy":
            print("Pay $3.")
        elif weather=="sunny":
            print("Pay $7.")
        elif weather=="snowing":
            print("Pay $6.50.")
        elif weather=="hailing":
            print("You're in for free!")
        else:
            print("Pay $5.")
    elif age=="high school":
        if weather=="rainy":
            print("Pay $5.")
        elif weather=="sunny":
            print("Pay $9.")
        elif weather=="snowing":
            print("Pay $8.50.")
        elif weather=="hailing":
            print("You're in for free!")
        else:
            print("Pay $7.")
    else:
        if weather=="sunny":
            print("Pay $10.")
        elif weather=="rainy":
            print("Pay $14.")
        elif weather=="snowing":
            print("Pay #13.50.")
        elif weather=="hailing":
            print("You're in for free!")
        else:
            print("Pay $12.")

    print("Thanks for coming to the movies!")

movies()
