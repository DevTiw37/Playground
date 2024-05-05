name = input("Enter your name: ")
print(f"Hello! {name}, thankyou so much for coming in today.\n")
rder = input(f"{name}, what would you like from our menu today? Here is what we are serving.\nBlack Coffee, Espresso, Latte, Cappuciro\n")
menu = ["Black Coffee", "Espresso", "Latte", "Cappuciro"]
try:
    for i in menu:
        if i.lower() == order.lower():
            print(f"Sounds great {name}! Your {order} will be ready soon.")

except:
    print("Sorry! we don't serve this")
