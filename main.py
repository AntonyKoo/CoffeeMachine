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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)  # round 소수점 계산
        print(f"Here is ${change} in charge.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")



def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please, insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_resource_sufficient(order_ingredients):  # 이 함수는 T/F를 return 하는 함수
    for item in order_ingredients:  # for loop에 사전형을 담으면, 개별 인자는 key가 담긴다.
        if order_ingredients[item] > resources[item]:  ### >=가 아닌게 맞지?
            print(f"Sorry, there is not enough {item}.")
            return False
    return True  # if 구문이 작동하지 않는 경우.


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice not in ["latte", "espresso", "cappuccino"]:
        pass
    else:
        drink = MENU[choice]  # key가 "ingredient", "cost"인 dictionary data
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()  # inserted coins의 total을 알았으니, 돈계산 해야 함.
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
