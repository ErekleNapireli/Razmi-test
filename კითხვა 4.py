#4)შემოიტანე 2 input შეამოწმე, არის თუ არა ორი რიცხვის ჯამი 100-ზე მეტი.

num1 = int(input("Enter the first number here:"))
num2 = int(input("Enter the second number here:"))
if num1 + num2 > 100:
    print("Sum of the both numbers is greater than 100")
elif num1 + num2 < 100:
    print("Sum of the both numbers is NOT greater than 100")
else:
    print("Sum of the both numbers is equal to 100")