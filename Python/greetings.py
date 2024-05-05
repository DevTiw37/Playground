import time
name = input("Enter your name: ")
Cname = name.title()
getTime = int(time.strftime("%H"))
timestamp = time.strftime("%H:%S:%M %p, %d-%m-%Y")
if 4 <= getTime < 12:
    print(f"Good morning {Cname}! It's {timestamp}")
elif 12 <= getTime < 17:
    print(f"Good afternood {Cname}! It's {timestamp}")
elif 17 <= getTime < 22:
    print(f"Good evening {Cname}! It's {timestamp}")
else:
    print(f"Good Night {Cname}! It's {timestamp}")