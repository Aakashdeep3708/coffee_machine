import main

profit=0
continue_machine=True
choice=main.MENU
report=main.resources

def total_payment():
    print("Please insert coin")
    rupee_1=int(int(input("number of 1 rupee coins:"))*1)
    rupee_2=int(int(input("number of 2 rupee coins:"))*2)
    rupee_5=int(int(input("number of 5 rupee coins:"))*5)
    rupee_10=int(int(input("number of 10 rupee coins:"))*10)
    sum=rupee_1+rupee_2+rupee_5+rupee_10
    return sum

def resource_sufficient(ingredient):
    for i in ingredient:
        if ingredient[i]>report[i]:
            print(f"there is not sufficient resource {i}")
            return False
    return True

def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change =money_received - drink_cost
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def coffee_making(order,drink_ingredients):
    for i in drink_ingredients:
        report[i]-=drink_ingredients[i]
    print(f"here is your {order} ready")

while continue_machine:
    order=input("What would you like ? (espresso/latte/cappuccino)")
    if order=="off":
        continue_machine=False
    elif order=="report":
        print(report)
        print(profit)
    else:
        drink=choice[order]
        if resource_sufficient(drink['ingredients']):
            payment=total_payment()
            if transaction_successful(payment,drink['cost']):
                coffee_making(order,drink["ingredients"])






