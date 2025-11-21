database = ["Wendy", "Alice", "Bob", "Mia"]
name = input("What is your name? ")
if name in database:
    print(f"Hello, {name}")
else:
    print("Sorry, I don’t know you.")
