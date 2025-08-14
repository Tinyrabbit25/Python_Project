# Python compound interest calculator

principal = 0
rate =  0
time = 0

while True: # Using while true but not some condition to let the user enter in 0's
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("principal can't be less than 0")
    else:
        break # Explicitly breaking the loop so there's no condition that is false
while True:
    rate = float(input("Enter the interest rate: "))
    if rate <0:
        print("Rate can't be less than 0")
    else:
        break # same as before

while True:
    time = int(input("Enter your time in years: "))
    if time <0:
        print("Time can't be less than")
    else:
        break # same as before

total = principal * pow((1 + rate/100), time) # Calculating the compound interest
print(f"Balance after {time} year/s: ${total:.2f}") # prints the total interest