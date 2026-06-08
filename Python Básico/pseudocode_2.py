"""Time"""

time = int(input("Enter the time: "))
seconds_remaining = 0

if time < 600:
    seconds_remaining = 600 - time
    print(f"{seconds_remaining} seconds left")
elif time > 600:
    print("Is older")
else:
    print("Is equal")
