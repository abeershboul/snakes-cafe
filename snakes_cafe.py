def order():
    
    while True:
        order_input = input('> ').title()
        if order_input.lower() == 'quit':
            
            print('Wellcome!')
            break
        if order_input in orders:
            orders[order_input] += 1
            if orders[order_input] == 1:
                print(f'** {orders[order_input]} order of {order_input} has been added to your meal **')
            else:
                print(f'** {orders[order_input]} orders of {order_input} have been added to your meal **')
        else:
            print(f'Sorry,{order} is not in the Menu ')

    print("Your  order is: ")
    for x in orders:
                if orders[x] > 0:
                    
                    print(f' {orders[x]} orders of {x}')
        


orders = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
    }
MENU = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Beverages
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************'''

print(MENU)
order()

