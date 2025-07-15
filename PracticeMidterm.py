# Emily Smith
# Practice Mid Term

# Welcome message for the customer
print("Welcome to Catrinas Mexican Grill! Build your own taco!")

# List of available tortilla types
tortilla_types = ["Corn", "Flour", "Whole Wheat"]

# List of available fillings
filling_types = ["Beans", "Chicken", "Fish", "Beef"]

# List of available toppings
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]

# Function to show the list of choices with numbers
def display_options(options):
    i = 1
    for option in options:
        print(str(i) + ". " + option)
        i += 1

# Function to get the user's choice from a list
def get_choice(options):
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice >= 1 and choice <= len(options):
                return options[choice - 1]
            else:
                print("Please enter a number from the list.")
        except ValueError:
            print("That was not a number. Please try again.")

# Ask the user to choose a tortilla
print("Choose your tortilla:")
display_options(tortilla_types)
chosen_tortilla = get_choice(tortilla_types)
print("You selected: " + chosen_tortilla)
print()

# Ask the user to choose a filling
print("Choose your filling:")
display_options(filling_types)
chosen_filling = get_choice(filling_types)
print("You selected: " + chosen_filling)
print()

# Let the user pick multiple toppings
chosen_toppings = []  # This list will store the selected toppings
print("Choose your toppings (type 0 to finish):")

while True:
    display_options(toppings)
    print("0. Done selecting toppings")

    try:
        topping_input = int(input("Enter the number of your topping choice: "))

        if topping_input == 0:
            break
        elif topping_input >= 1 and topping_input <= len(toppings):
            selected_topping = toppings[topping_input - 1]
            if selected_topping not in chosen_toppings:
                chosen_toppings.append(selected_topping)
                print(selected_topping + " added.")
                print()
            else:
                print("You already chose " + selected_topping + ".")
                print()
        else:
            print("Please choose a number from the list.")
    except ValueError:
        print("That was not a number. Please try again.")

# Show the final order summary
print("\nYour Taco Order is:")
print("Tortilla: " + chosen_tortilla)
print("Filling: " + chosen_filling)
print("Toppings: " + ", ".join(chosen_toppings))

# Check if "Salsa" is in the toppings list
if "Salsa" in chosen_toppings:
    print("One spicy salsa taco coming up!")

# Final thank you message
print("\nThank you for ordering from Catrinas Mexican Grill!")
