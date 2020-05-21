***
#### About:

Programming a **Coffee Machine Simulator.** 

The machine works with typical products: coffee, milk, sugar, and plastic cups; if it runs out of something, it shows a 
notification. You can get three types of coffee: espresso, cappuccino, and latte. it also collects the money.

Coffee machine has the the initial resources as in the example (400 ml of water, 540 ml of milk, 120 g of 
coffee beans, 9 disposable cups, $550 in cash.

- For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
- For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
- And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.

 
####**Example 1:**

Write action (buy, fill, take, remaining, exit):
> remaining
 
`The coffee machine has:`

`400 of water`

`540 of milk`

`120 of coffee beans`

`9 of disposable cups`

`$550 of money`

Write action (buy, fill, take, remaining, exit):
> buy
 
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
>
`I have enough resources, making you a coffee!`
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
`The coffee machine has:`

`50 of water`

`465 of milk`

`100 of coffee beans`

`8 of disposable cups`

`$557 of money`
 
Write action (buy, fill, take, remaining, exit):
> buy
 
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2

`Sorry, not enough water!`

 
Write action (buy, fill, take, remaining, exit):
> fill
 
Write how many ml of water do you want to add:
> 1000

Write how many ml of milk do you want to add:
> 0

Write how many grams of coffee beans do you want to add:
> 0

Write how many disposable cups of coffee do you want to add:
> 0
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
`The coffee machine has:`

`1050 of water`

`465 of milk`

`100 of coffee beans`

`8 of disposable cups`

`$557 of money`
 
Write action (buy, fill, take, remaining, exit):
> buy
 
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2

`I have enough resources, making you a coffee!`
 
Write action (buy, fill, take, remaining, exit):
> remaining

`The coffee machine has:`

`700 of water`

`390 of milk`

`80 of coffee beans`

`7 of disposable cups`

`$564 of money`
 
Write action (buy, fill, take, remaining, exit):
> take
 
`I gave you $564`
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
`The coffee machine has:`

`700 of water`

`390 of milk`

`80 of coffee beans`

`7 of disposable cups`

`$0 of money`
 
Write action (buy, fill, take, remaining, exit):
> exit
***