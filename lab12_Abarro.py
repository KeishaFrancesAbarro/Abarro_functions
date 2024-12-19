def display_menu():
    menu= {
        1: ("Ice cream", 3.99) ,
        2: ("French Fries", 2.99) ,
        3: ("Salad" , 4.99) ,
        4: ("Pizza" , 8.99) , 
        5: ("Burger" , 7.99) , 
    }
    print("\nMenu: ")
    for product_number, (product_name, price) in menu.items() :
        print(f"{product_number}. {product_name} - ${price:.2f}")
    return menu

def get_order(menu):
    while True:
        try :
            choice = int(input("\nEnter the number of the items that you would love to buy: "))
            if choice in menu:
                product_name, price = menu [choice]
                print(f"You have selected: {product_name} - ${price:.2f}") 
                return price
            else:
                print("Choice is invalid. Please choose a valid product")
        except ValueError:
            print("Input is invalid. Please enter a number")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nYour total is ${total_cost:.2f}. Enter amount of cash: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment is accepted. Your change would be ${change:.2f}. Thanks so much!!!")
                break
            else:
                print(f"Your amount is insufficeient. You need ${total_cost:.2f}. Please try again.")
        except ValueError:
            print("Your input is invalid. Please try to enter a valid amount.")

def main():
    print("Hello, Welcome to our food ordering system!!! ")
    menu = display_menu()
    total_cost = get_order(menu)
    process_payment(total_cost)

if __name__ == "__main__":
    main()