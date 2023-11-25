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

COINS = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_report():
    for resource in resources:
        unit = ''
        if resource == 'water' or resource == 'milk':
            unit = 'ml'
            print(f'{resource.title()}: {resources[resource]}{unit}')
        elif resource == 'coffee':
            unit = 'g'
            print(f'{resource.title()}: {resources[resource]}{unit}')
        else:
            unit = '$'
            print(f'{resource.title()}: {unit}{resources[resource]}')


def check_resources(drink):
    for resource in resources:
        if resource in MENU[drink]['ingredients']:
            if MENU[drink]['ingredients'][resource] > resources[resource]:
                print(f'Sorry, there is not enough {resource}')
                return False
    return True


def get_money(drink):
    enough_money = False
    cost_of_drink = MENU[drink]['cost']
    current_amount = 0
    current_amount += take_coins()
    if current_amount > cost_of_drink:
        print(f'Please take change of {round(current_amount - cost_of_drink, 2)}')
        enough_money = True
    elif current_amount < cost_of_drink:
        print(f'You did not put enough money. Money was refunded')
    else:
        print(f'Exact amount. Brilliant!')
        enough_money = True
    if enough_money:
        if 'money' in resources:
            current_money = resources["money"]
            current_money += MENU[drink]['cost']
            resources["money"] = current_money
        else:
            resources["money"] = MENU[drink]['cost']
    return enough_money


def take_coins():
    quarters_amount = int(input('Put quarters: ')) * 0.25
    dimes_amount = int(input('Put dimes: ')) * 0.1
    nickles_amount = int(input('Put nickles: ')) * 0.05
    pennies_amount = int(input('Put pennies: ')) * 0.01
    return round((quarters_amount + dimes_amount + nickles_amount + pennies_amount), 2)


def deduct_resources(drink):
    for resource in resources:
        if resource in MENU[drink]['ingredients']:
            resources[resource] -= MENU[drink]['ingredients'][resource]


def make_drink(drink):
    enough_money = get_money(drink)
    if enough_money:
        deduct_resources(drink)
        print(f'Here is your {drink}. Enjoy!')


working_now = True

while working_now:
    next_action = input('What would you like? (espresso/latte/cappuccino): ')
    if next_action == 'report':
        make_report()
    elif next_action in ('espresso', 'latte', 'cappuccino'):
        if check_resources(next_action):
            make_drink(next_action)
    else:
        working_now = False
