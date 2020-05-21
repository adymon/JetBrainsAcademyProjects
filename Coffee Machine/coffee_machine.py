# Write your code here

"""
# Step 1
# Coffee making steps

print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")


# Step 2
# Number of coffee drinks

coffee_cups = int(input("Write how many cups of coffee you will need:\n"))
water = 200 * coffee_cups
milk = 50 * coffee_cups
coffee_beans = 15 * coffee_cups

print(f"For {coffee_cups} cups of coffee you will need:\n{water} ml of water\n{milk} ml of milk\n{coffee_beans} g of"
      f" coffee beans")

# Step 3
# Coffee machine capacity

total_water = int(input("Write how many ml of water the coffee machine has:\n"))
total_milk = int(input("Write how many ml of milk the coffee machine has:\n"))
total_beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
coffee_cups = int(input("Write how many cups of coffee you will need:\n"))

min_water = total_water // 200
min_milk = total_milk // 50
min_beans = total_beans // 15
select_min = min(min_water, min_milk, min_beans)

water = 200 * coffee_cups
milk = 50 * coffee_cups
coffee_beans = 15 * coffee_cups

# Example 3
if total_water > water and total_milk > milk and total_beans > coffee_beans and coffee_cups >= 0:

    print(f"Yes, I can make that amount of coffee (and even {select_min - 1} more than that)")

# Example 2
elif total_water < water or total_milk < milk or total_beans < coffee_beans:

    print(f"No, I can make only {select_min} cup(s) of coffee")

# Example 4
elif total_water == 0 and total_milk == 0 and total_beans == 0 and coffee_cups >= 1:
    print("No, I can make only 0 cup(s) of coffee")

# Example 5
elif total_water == 0 and total_milk == 0 and total_beans == 0 and coffee_cups == 0:
    print("Yes, I can make that amount of coffee")


# Example 6
elif total_water > water and total_milk > milk and total_beans > coffee_beans and coffee_cups == 0:

    print(f"Yes, I can make that amount of coffee (and even {select_min} more than that)")


# Example 1
elif (1 <= total_water / water < 2 or 1 <= total_milk / milk < 2 or 1 <= total_beans / coffee_beans < 2) and coffee_cups \
        == 1:
    print("Yes, I can make that amount of coffee")


# Step 4 & 5
# Full working flow

total_water = 400
total_milk = 540
total_beans = 120
coffee_cups = 9
total_money = 550


def coffee_machine_capacity():
    print(
        f"The coffee machine has:\n{total_water} of water\n{total_milk} of milk\n{total_beans} of coffee beans\n{coffee_cups} of disposable cups\n{total_money} of money\n")


coffee_machine_capacity()


def buy(a):
    if a == "1":
        print(
            f"\nThe coffee machine has:\n{total_water - 250} of water\n{total_milk} of milk\n{total_beans - 16} of coffee beans\n{coffee_cups - 1} of disposable cups\n{total_money + 4} of money")

    elif a == "2":
        print(
            f"\nThe coffee machine has:\n{total_water - 350} of water\n{total_milk - 75} of milk\n{total_beans - 20} of coffee beans\n{coffee_cups - 1} of disposable cups\n{total_money + 7} of money")

    elif a == "3":
        print(
            f"\nThe coffee machine has:\n{total_water - 200} of water\n{total_milk - 100} of milk\n{total_beans - 12} of coffee beans\n{coffee_cups - 1} of disposable cups\n{total_money + 6} of money")

    elif a == "back":
        pass


def fill():
    add_water = int(input("Write how many ml of water do you want to add:\n"))
    add_milk = int(input("Write how many ml of milk do you want to add:\n"))
    add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

    print(
        f"\nThe coffee machine has:\n{total_water + add_water} of water\n{total_milk + add_milk} of milk\n{total_beans + add_beans} of coffee beans\n{coffee_cups + add_cups} of disposable cups\n{total_money} of money")


def take():
    print(f"I gave you ${total_money}\n")
    print(
        f"The coffee machine has:\n{total_water} of water\n{total_milk} of milk\n{total_beans} of coffee beans\n{coffee_cups} of disposable cups\n{total_money - total_money} of money")


action = input("Write action (buy, fill, take, remaining, exit):\n")
for i in action:

    if action == "buy":
        buy(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        coffee_machine_capacity()
    elif action == "exit":
        break

"""


# Combined Steps - Making a coffee Machine Program using Object Oriented Programming

class CoffeeMachine:

    def __init__(self):
        self.total_water = 400
        self.total_milk = 540
        self.total_beans = 120
        self.coffee_cups = 9
        self.total_money = 550

    def action(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        return action

    def coffee_machine_capacity(self):
        print(
            f"The coffee machine has:\n{self.total_water} of water\n{self.total_milk} of milk\n{self.total_beans} of coffee beans\n{self.coffee_cups} of disposable cups\n${self.total_money} of money\n")

    def buy(self, a):

        if a == "1":
            if self.total_water < 250:
                print("Sorry, not enough water!")
            elif self.total_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.coffee_cups < 1:
                print("Sorry, not enough disposable cups!")

            else:
                print("I have enough resources, making you a coffee!")

                self.total_water -= 250
                self.total_beans -= 16
                self.coffee_cups -= 1
                self.total_money += 4

        elif a == "2":
            if self.total_water < 350:
                print("Sorry, not enough water!")
            elif self.total_milk < 75:
                print("Sorry, not enough milk!")
            elif self.total_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.coffee_cups < 1:
                print("Sorry, not enough disposable cups!")

            else:
                print("I have enough resources, making you a coffee!")

                self.total_water -= 350
                self.total_milk -= 75
                self.total_beans -= 20
                self.coffee_cups -= 1
                self.total_money += 7

        elif a == "3":
            if self.total_water < 200:
                print("Sorry, not enough water!")
            elif self.total_milk < 100:
                print("Sorry, not enough milk!")
            elif self.total_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.coffee_cups < 1:
                print("Sorry, not enough disposable cups!")

            else:
                print("I have enough resources, making you a coffee!")

                self.total_water -= 200
                self.total_milk -= 100
                self.total_beans -= 12
                self.coffee_cups -= 1
                self.total_money += 6

        elif a == "back":
            pass

    def remaining(self):
        self.coffee_machine_capacity()

    def fill(self):

        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

        self.total_water += add_water
        self.total_milk += add_milk
        self.total_beans += add_beans
        self.coffee_cups += add_cups

    def take(self):
        print(f"I gave you ${self.total_money}\n")

        self.total_money = 0


CM = CoffeeMachine()

while True:
    action = CM.action()

    if action == "buy":
        CM.buy(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
    elif action == "fill":
        CM.fill()

    elif action == "remaining":
        CM.coffee_machine_capacity()

    elif action == "take":
        CM.take()
    else:
        break
