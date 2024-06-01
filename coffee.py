MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Rate card -\n Espresso $1.50 \n Latte $2.50 \n Cappuccino $3.50")
coffee_type = input("What would you like? Espresso/Latte/Cappuccino\n")

print("Penny = $0.01\nDime = $0.10 \nNickel = $0.05 \nQuarter = $0.25")
print("Please insert coins...")
penny = int(input("Please insert penny coins: "))
dime = int(input("Please insert dime coins: "))
quarter = int(input("Please insert quarter coins: "))
nickel = int(input("Please insert nickel coins: "))
total_money = ((penny * 0.01) + (dime * 0.10) + (quarter * 0.25) + (nickel * 0.05))
print(f'Total money inserted: ${total_money:.2f}')

if coffee_type.lower() in MENU:
    cost = MENU[coffee_type.lower()]["cost"]
    if total_money >= cost:
        change = total_money - cost
        print(f'Here is your {coffee_type} ☕. Enjoy!')
        print(f'Your change: ${change:.2f}')
        # Update resources
        for ingredient, quantity in MENU[coffee_type.lower()]["ingredients"].items():
            resources[ingredient] -= quantity
        print(f'Remaining resources: {resources}')
    else:
        print("Not enough money. Refunding...")
else:
    print("Invalid choice. Please choose from Espresso, Latte, or Cappuccino.")

